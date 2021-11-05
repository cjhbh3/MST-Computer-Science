//Programmer: CJ Hess  Date: 01/28/2020
//File: Lab02.cpp  Class: Section 303
//Description: Looking for compilation errors and syntactical errors

#include <iostream>
using namespace std;

int main()
{
  //Variable declaration
  int input_1;  //A number
  int input_2;  //Another  number
  int add_res;  //This stores th first operation
  int subtraction_results;  //This stores the second operation
  int multiplication_results;  //This stores the third operation
  int division_result;  //This stores th fourth operation
  
  cout<<"Welcome to the math basic tutorial"<<endl;
  cout<<"Please input two numbers"<<endl;
  cin>>input_1; //This takes in a thing
  cin>>input_2;  //This also takes in a thing
  add_res = input_1 + input_2;  //This performs the operation on the numbers
  cout<<"Adding the two numbers gives us: "<<add_res<<endl;  //This outputs to the screen
  subtraction_results = input_1 - input_2; //This performs the operation on the numbers
  cout<<"Subtracting input 2 from input 1 gives you: "<<subtraction_results<<endl;  //This outputs to the screen
  multiplication_results = input_1 * input_2;  //This performs the operation on the numbers
  cout<<"Multiplying the two numbers together gives us: "<<multiplication_results<<endl; //This outputs to the screen
  division_result = input_1/input_2;  //This perfomrs the operation on the numbers
  cout<<"Dividing number 1 by number 2 gives us: "<<division_result<<endl;  //This outputs to the screen

return 0;

}
