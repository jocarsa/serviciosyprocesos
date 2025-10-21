onmessage = function(){
  let numero = 1.0000000000534;
  for(let i = 0;i<10000000000000;i++){
    numero *= 1.00000000053;
  }
  postMessage("Ya he terminado")
}
