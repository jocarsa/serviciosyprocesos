onmessage = function(datos){            // Cuando escuche un mensaje
  console.log(datos)
  misdatos = []
  for(let i = 0;i<datos.data.length;i+=4){   // Recorro los datos
    misdatos[i] = 255-datos.data[i];            // Invierto el canal rojo
    misdatos[i+1] = 255-datos.data[i+1];        // Invierto el canal verde
    misdatos[i+2] = 255-datos.data[i+2];        // Invierto el canal azul
  }
  postMessage(misdatos)                    // Devuelvo los datos
}
