import os
import zipfile
import shutil
import sys
import time
from datetime import datetime
from functools import partial
from pathlib import Path
import multiprocessing as mp

#### CUIDADO CON ESTE PROGRAMA
#### USALO BIEN
#### UN GRAN PODER CONLLEVA UNA GRAN RESPONSABILIDAD

'''
  Multiproceso:
  - Reparte por procesos los ítems de primer nivel (carpetas/archivos) de la ruta indicada.
  - Cada proceso comprime su ítem a ZIP.
  - Opción para borrar originales tras éxito.
  - Barra de progreso con porcentaje y ETA en el proceso padre.
'''

# ======= Ajustes =======
borrar_originales = False          # ponlo a False para conservar los originales
compresion = zipfile.ZIP_DEFLATED  # ZIP_STORED, ZIP_DEFLATED, ZIP_BZIP2, ZIP_LZMA
compresslevel = 6                  # 1-9 (si tu Python/zipfile lo soporta)
respetar_zip_existente = True      # si True, crea nombre alternativo si ya existe el .zip

# ======= Utilidades barra de progreso =======
def formatear_tiempo(segundos: float) -> str:
    segundos = int(segundos)
    h = segundos // 3600
    m = (segundos % 3600) // 60
    s = segundos % 60
    if h > 0:
        return f"{h:02d}:{m:02d}:{s:02d}"
    else:
        return f"{m:02d}:{s:02d}"

def mostrar_progreso(procesados, total, inicio):
    if total == 0:
        return
    porcentaje = (procesados / total)
    ancho_barra = 30
    rellenos = int(ancho_barra * porcentaje)
    barra = "[" + "#" * rellenos + "-" * (ancho_barra - rellenos) + "]"

    transcurrido = time.time() - inicio
    if procesados > 0:
        estimado_total = transcurrido / max(procesados, 1) * total
        restante = max(0, estimado_total - transcurrido)
    else:
        restante = 0

    texto = (
        f"\r{barra} {porcentaje*100:6.2f}%  "
        f"transcurrido: {formatear_tiempo(transcurrido)}  "
        f"restante: {formatear_tiempo(restante)}"
    )
    sys.stdout.write(texto)
    sys.stdout.flush()

# ======= Trabajo de cada proceso =======
def nombre_zip_destino(origen: Path) -> Path:
    """Devuelve el path del ZIP a crear (origen + '.zip').
       Si ya existe y 'respetar_zip_existente' es True, genera nombre alternativo con timestamp."""
    base = origen.with_suffix(origen.suffix + ".zip") if origen.is_file() else Path(str(origen) + ".zip")
    if not base.exists():
        return base
    if not respetar_zip_existente:
        # Sobrescribe
        return base
    # Genera alternativo
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    return base.with_name(base.stem + f"_{ts}" + base.suffix)

def comprimir_carpeta(origen: Path, destino_zip: Path):
    # Nota: arcname relativo a la carpeta 'origen' para mantener estructura interna
    with zipfile.ZipFile(destino_zip, 'w', compression=compresion, compresslevel=compresslevel) as zf:
        for directorio, _, archivos in os.walk(origen):
            d = Path(directorio)
            for archivo in archivos:
                rutaarchivo = d / archivo
                rutarelativa = rutaarchivo.relative_to(origen)
                zf.write(rutaarchivo, arcname=str(rutarelativa))

def comprimir_archivo(origen: Path, destino_zip: Path):
    with zipfile.ZipFile(destino_zip, 'w', compression=compresion, compresslevel=compresslevel) as zf:
        zf.write(origen, arcname=origen.name)

def worker(origen_str: str, borrar: bool) -> tuple:
    """Procesa un único ítem (carpeta o archivo). Devuelve (ok:bool, origen, destino_zip, error:str|None)."""
    origen = Path(origen_str)
    try:
        # Evitar ZIPs de entrada
        if origen.is_file() and origen.suffix.lower() == ".zip":
            return (True, str(origen), None, None)  # lo consideramos "no-op correcto"

        destino = nombre_zip_destino(origen)

        if origen.is_dir():
            comprimir_carpeta(origen, destino)
            if borrar:
                shutil.rmtree(origen)
        elif origen.is_file():
            comprimir_archivo(origen, destino)
            if borrar:
                origen.unlink(missing_ok=True)
        else:
            return (False, str(origen), None, "No es archivo ni carpeta")

        return (True, str(origen), str(destino), None)

    except Exception as e:
        return (False, str(origen), None, f"{type(e).__name__}: {e}")

# ======= Main =======
def main():
    ruta = input("Introduce la ruta de la carpeta: ").strip()
    base = Path(ruta)

    if not base.is_dir():
        print("La ruta no es válida")
        return

    # Listado primer nivel, excluyendo .zip
    items = []
    for nombre in os.listdir(base):
        p = base / nombre
        if p.is_file() and p.suffix.lower() == ".zip":
            continue
        items.append(str(p))

    total = len(items)
    if total == 0:
        print("No hay elementos que procesar.")
        return

    print(f"Procesando {total} ítems con multiproceso…")

    inicio = time.time()
    procesados = 0
    mostrar_progreso(procesados, total, inicio)

    # Tamaño del pool: núcleos disponibles (pero no más que ítems)
    workers = min(mp.cpu_count(), total)
    worker_fn = partial(worker, borrar=borrar_originales)

    # Pool + progreso en el padre conforme van llegando resultados
    exitos = 0
    fallos = 0

    try:
        with mp.Pool(processes=workers) as pool:
            for ok, origen, destino, err in pool.imap_unordered(worker_fn, items, chunksize=1):
                procesados += 1
                if ok:
                    exitos += 1
                else:
                    fallos += 1
                    # Puedes descomentar para ver el detalle de cada error
                    # print(f"\nError con {origen}: {err}")
                mostrar_progreso(procesados, total, inicio)

    except KeyboardInterrupt:
        print("\nInterrumpido por el usuario. Cancelando trabajos en curso…")
        # Pool se cierra por el context manager
    except Exception as e:
        print(f"\nHa habido un error general: {type(e).__name__}: {e}")

    print()  # salto de línea al terminar la barra
    print(f"Proceso completado. Éxitos: {exitos}, Fallos: {fallos}.")

if __name__ == "__main__":
    # Requerido para Windows y buena práctica en multiproceso
    mp.freeze_support()
    main()

