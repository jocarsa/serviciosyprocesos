#include <iostream>
#include <string>
using namespace std;

double suma(double operando1,double operando2){
  double resultado = operando1 + operando2;
  return resultado;
}

int main(){
  cout << suma(4.5,3.3) << "\n";
  cout << suma(7,6) << "\n";
  return 0;
}

