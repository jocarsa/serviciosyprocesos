#include <iostream>
#include <string>

using namespace std;

int main(){

  double numero = 1.000000000043;
  for(int i = 0;i<1000000000000000;i++){
    numero = numero * 1.000000000000000324;
  }
  cout << "ya he terminado";
  
  return 0;
}
