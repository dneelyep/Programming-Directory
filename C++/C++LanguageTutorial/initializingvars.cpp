// initializing variables
// Might be helpful to run the program to understand it better - all the 'cout's below explain the program's behavior while it's running.

#include <iostream>
using namespace std;

int main ()
{
  int a = 5; 	// initializing 'a' to = 5
  int b (2);	// initializing 'b' to = 2, using a different method than that used in 'a' (both still work though)
  int result;	// and declaring another variable, with no initial value

  cout << "The variable 'a' has been initialized as:";
  cout << a;
  cout << "The variable 'b' has been initialized as:";
  cout << b;
  a = a + 3;
  cout << "setting 'a' equal to 'a' + 3 =";
  cout << a;
  result = a - b;
  cout << "The result of 'a' minus 'b' =";
  cout << result;

  return 0;	//QUEET!
}
