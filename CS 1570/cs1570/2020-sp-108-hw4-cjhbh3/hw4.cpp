// Name: CJ Hess
// Date: February 16th, 2020
// File: hw4.cpp
// Purpose: The purpose of this program is to present the user with three
// options. Enter a number, power the number, and cube root the number.
// Depending on the option, the program takes in input and calculates 
// the chosen option.
# include <iostream>
using namespace std;

int main()
{
  // Variable declarations and constants
  int menuChoice, numberRaised, base, exponent;
  double cubeRooted;
  bool quitMenu = false;
  bool numberInputed = false;
  // Greeting
  cout << "Welcome back Groundskeeper! Lets do some math" << endl;
  // Intro Menu
  while (!quitMenu) // While option 4 has not been selected
  {
    cout << "Menu" << endl;
    cout << "----" << endl;
    cout << "1. Enter a number" << endl;
    cout << "2. Power the number" << endl;
    cout << "3. Cube root of the number" << endl;
    cout << "4. Quit" << endl;
    cin >> menuChoice;
    while (!(menuChoice >= 1 && menuChoice <= 4)) 
    { // Check that menu choice is valid
      cout << "Invalid Input!" << endl;
      cout << "Menu" << endl;
      cout << "----" << endl;
      cout << "1. Enter a number" << endl;
      cout << "2. Power the number" << endl;
      cout << "3. Cube root of the number" << endl;
      cout << "4. Quit" << endl;
      cin >> menuChoice;
    }
    switch (menuChoice)
    {
      case 1: // Entering a number
        cout << "Please enter a number: " << endl;
        cin >> base;
        while (base < 0) // Must be a positive number
        {
          cout << "Invalid Input!" << endl;
          cin >> base;
        }
        numberInputed = true;
        break;
      case 2: // Raising a number
        if (numberInputed) // If option 1 has been chosen
        {
          cout << "Please enter an exponent: " << endl;
          cin >> exponent;
          while (exponent < 0) // Must be a positive number
          {
            cout << "Invalid Input!" << endl;
            cin >> exponent;
          }
          numberRaised = base;
          for (int i = 1; i < exponent; i++)
          {
            numberRaised = numberRaised * base;
          }
          cout << base << " raised to " << exponent << " equals " 
          << numberRaised << endl;
        }
        else // If option 1 has not been chose
        {
          cout << "You have not entered a number." << endl;
        }
        break;
      case 3: // Cube root of a number
        if (numberInputed) // If option 1 has been chosen
        {
          for (int i = 0; i <= 10; i++)
          {
            if (i == 0)
            {
              cubeRooted = base; // First iteration, set value to base
            }
            else
            {
              cubeRooted = (2 * cubeRooted + base / 
              (cubeRooted * cubeRooted)) / 3.0;
            }
          }
          cout << "The cube root of " << base << " is " << cubeRooted << endl;
        }
        else // If option 1 has not been chose
        {
          cout << "You have not entered a number." << endl;
        }
	      break;
      case 4:
        cout << "Thank you for using the calculator." << endl;
        quitMenu = true;
      	break;
    }
  }
  // Signing off message
  cout << "Have a good day, Groundskeeper." << endl;
  // Return value
  return 0;
}
