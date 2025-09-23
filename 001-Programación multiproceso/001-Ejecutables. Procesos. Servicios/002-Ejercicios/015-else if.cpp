#include <iostream>
#include <string>
using namespace std;

int main(){
  int edad = 47;
  
  if(edad < 10){
    cout << "Eres un niño" << "\n";
  }else if(edad >= 10 && edad < 20){
    cout << "Eres un adolescente" << "\n";
  }else if(edad >= 20 && edad < 30){
    cout << "Eres un joven" << "\n";
  }else{
    cout << "Ya no eres un joven" << "\n";
  }
  
  return 0;
}

