#include <iostream>
#include <string>
using namespace std;

int main(){
  // Primero creamos variables
  
  double peso_boxeador;
  string categoria;
  
  // El usuario introduce información
  
  cout << "Introduce el peso del boxeador" << "\n";
  cin >> peso_boxeador;
  cout << "El boxeador pesa " << peso_boxeador << "\n"; 
  
  // Segundo realizamos cálculos
  
  if(peso_boxeador < 52){
    categoria = "Mosca";
  }else if(peso_boxeador >= 52 && peso_boxeador < 60){
    categoria = "Ligero";
  }else if(peso_boxeador >= 60 && peso_boxeador < 69){
    categoria = "Wélter";
  }else if(peso_boxeador >= 69 && peso_boxeador < 75){
    categoria = "Medio";
  }else{
    categoria = "Pesado";
  }
  
  // Devolvemos un resultado
  
  cout << "El boxeador pertenece a la categoría: " << categoria << "\n";
  
  return 0;
}

