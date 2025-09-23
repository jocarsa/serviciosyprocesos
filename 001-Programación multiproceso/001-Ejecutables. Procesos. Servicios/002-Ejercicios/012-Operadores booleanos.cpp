#include <iostream>
#include <string>
using namespace std;

int main(){
 int edad = 47;
  cout << (4 == 4 && 3 == 3 && 2 == 2) << "\n";
  cout << (4 == 4 && 3 == 3 && 2 == 1) << "\n";
  
  cout << (4 == 4 || 3 == 3 || 2 == 1) << "\n";
  cout << (4 == 4 || 3 == 2 || 2 == 1) << "\n";
  cout << (4 == 3 || 3 == 2 || 2 == 1) << "\n";
  return 0;
}

