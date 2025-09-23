#include <iostream>
#include <string>
using namespace std;

class Nave{
  public:
  string nombre_jugador;
  int puntuacion;
  Nave(string minombre, int mispuntos){
    nombre_jugador = minombre;
    puntuacion = mispuntos;
  }  
  void disparar(string nuevonombre){
    puntuacion += 10;
  }
  string recibirImpacto(){
    puntuacion -= 10;
  }
};

int main(){
  
  Nave nave1("Jose Vicente",100);
  Nave nave2("Jorge",100);
  
  return 0;
}

