### **Ejercicio: Calculadora de Descuentos con Funciones**

#### **Enunciado**
Escribe un programa en C++ que calcule el precio final de un producto después de aplicar un descuento, **usando funciones**. Las reglas para el descuento son las mismas que antes:

- **10% de descuento** si el precio es **≥ 100€**.
- **5% de descuento** si el precio es **≥ 50€ y < 100€**.
- **Sin descuento** si el precio es **< 50€**.

El programa debe:
1. Pedir al usuario el **precio original** del producto.
2. **Calcular el descuento** usando una función.
3. **Calcular el precio final** usando otra función.
4. Mostrar el **precio original**, el **descuento aplicado** (o mensaje si no hay) y el **precio final**.

---

#### **Requisitos técnicos**
- **Función `calcularDescuento`**:
  - Recibe el precio original como parámetro.
  - Devuelve el **porcentaje de descuento** (0, 5 o 10).
- **Función `calcularPrecioFinal`**:
  - Recibe el precio original y el porcentaje de descuento.
  - Devuelve el **precio final** después del descuento.
- **Función `mostrarResultado`**:
  - Recibe el precio original, el descuento y el precio final.
  - Muestra la información al usuario.
- Usa **`cout` y `cin`** para la interacción con el usuario.
- Incluye **comentarios** para explicar cada función y paso.

---

#### **Ejemplo de salida**
```plaintext
Introduce el precio original del producto: 75
---
Precio original: 75.00€
Descuento aplicado: 5%
Monto del descuento: 3.75€
Precio final: 71.25€
---
Introduce el precio original del producto: 120
---
Precio original: 120.00€
Descuento aplicado: 10%
Monto del descuento: 12.00€
Precio final: 108.00€
---
Introduce el precio original del producto: 30
---
Precio original: 30.00€
No se aplica descuento.
Precio final: 30.00€
```

---

#### **Criterios de evaluación**
- **Uso de funciones**: Cada función debe realizar una tarea específica y estar bien definida.
- **Correctitud**: El programa calcula y muestra correctamente el descuento y el precio final.
- **Claridad del código**: Las funciones y variables tienen nombres descriptivos y hay comentarios explicativos.
- **Interacción con el usuario**: El programa es fácil de usar y muestra la información de forma clara.

---

