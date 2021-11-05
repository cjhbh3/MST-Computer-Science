// Name: CJ Hess
// Section: 303
// Date: February 4th, 2020
// File: lab3.cpp
// Description: The program takes in 4 integers from user and performs a
// calculation. Then it outputs the calculated value in a float 
#include <iostream>
#include <math.h>
using namespace std;

int main()
{
  // Variables
  int input1;
  int input2;
  int input3;
  int input4;
  const float SQUARE_ROOT = 0.5;
  float output;

  // Greetings and inputs
  cout << "Hello and welcome to the slope calculator." << endl;
  cout << "Please input the four integers you desire to compute with." << endl;
  cout << "Input 1: " << endl;
  cin >> input1;
  cout << "Input 2: " << endl;
  cin >> input2;
  cout << "Input 3: " << endl;
  cin >> input3;
  cout << "Input 4: " << endl;
  cin >> input4;

  // Calculations

  output = pow((static_cast<float>(input1)+input2)/static_cast<float>(input3),
    SQUARE_ROOT);
  output = static_cast<int>(output) % input4;
  output = static_cast<float>(output);
  
  // Outputs
  cout << "The output of the equation is: " << output << endl;
  return 0;
} 
