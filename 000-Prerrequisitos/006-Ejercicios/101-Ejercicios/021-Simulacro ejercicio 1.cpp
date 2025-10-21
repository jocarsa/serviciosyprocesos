#include <iostream>
#include <string>

using namespace std;

int main(){

  // Primero declaro variables globales
  string nombre;
  string porcentaje_de_alcohol;
  
  // Ahora le pido al usuario su nombre
  cout << "Escribe tu nombre:";
  cin >> nombre;
  
  // A continuación le pido el porcentaje de alcohol
  cout << "Escribe el porcentaje de alcohol";
  cin >> porcentaje_de_alcohol;
  
  // Saco los datos por pantalla
  cout << "El nombre que has introducido es: " << nombre << "\n";
  cout << "El porcentaje que has introducido es: " << porcentaje_de_alcohol << "\n";
  
  // Convierto el porcentaje a double
  double porcentaje_numero = stod(porcentaje_de_alcohol);
  
  // Compruebo el rango de alcohol
  if(porcentaje_numero < 5){
    cout << "Es suave";
  }else if(porcentaje_numero >= 5 && porcentaje_numero <7){
    cout << "Es fuerte";
  }else{
    cout << "Es muy fuerte";
  }
  // Y el programa termina
  return 0;
}
