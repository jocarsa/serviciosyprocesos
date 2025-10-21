#include <iostream>
#include <string>
using namespace std;

class Gato{
  public:
  string nombre;
  Gato(string minombre){
    nombre = minombre;
  }  
  void setNombre(string nuevonombre){
    nombre = nuevonombre;
  }
  string getNombre(){
    return nombre;
  }
};

int main(){
  Gato gato1("micifu");
  cout << gato1.getNombre() << "\n";
  return 0;
}

