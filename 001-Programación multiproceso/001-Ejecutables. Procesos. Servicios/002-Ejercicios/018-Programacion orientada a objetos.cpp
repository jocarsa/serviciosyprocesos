#include <iostream>
#include <string>
using namespace std;

class Gato{
  public:
  string nombre;
  Gato(string minombre){
    nombre = minombre;
  }  
  
};

int main(){
  Gato gato1("micifu");
  cout << gato1.nombre << "\n";
  return 0;
}

