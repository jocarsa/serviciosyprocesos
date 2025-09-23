#include <iostream>
#include <string>

using namespace std;

int main(){
  string nombre;
  string porcentaje_de_alcohol;
  
  cout << "Escribe tu nombre:";
  cin >> nombre;
  
  cout << "Escribe el porcentaje de alcohol";
  cin >> porcentaje_de_alcohol;
  
  cout << "El nombre que has introducido es: " << nombre << "\n";
  cout << "El porcentaje que has introducido es: " << porcentaje_de_alcohol << "\n";
  
  double porcentaje_numero = stod(porcentaje_de_alcohol);
  
  if(porcentaje_numero < 5){
    cout << "Es suave";
  }else if(porcentaje_numero >= 5 && porcentaje_numero <7){
    cout << "Es fuerte";
  }else{
    cout << "Es muy fuerte";
  }
  return 0;
}
