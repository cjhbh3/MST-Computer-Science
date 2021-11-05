// Name: CJ Hess	Date: February 3,2020
// File: hw2.cpp
// Section: 108
// Purpose: For hw2, we are required to take in four inputs
// (wt, SF, L, IDIOTS, BP) and are supposed to output the length needed
// for Groundskeeper Willie and the fork he need to use (1-12)

#include <iostream>
using namespace std;

int main() 
{
  // Variables and Constants
  const int IDIOTS = 8;
  double weight;
  int stinkFactor;
  double lengthOfTail;
  double barometricPressure;
  double handleLength;
  int forkNumber;

  // Greeting and Input
  cout << "Welcome Groudskeeper! Let's find the correct pitchfork." << endl;
  cout << "What is the stink factor?" << endl;
  cin >> stinkFactor;
  cout << "What is the barometic pressure?" << endl;
  cin >> barometricPressure;
  cout << "What is the tail length?" << endl;
  cin >> lengthOfTail;
  cout << "What is the weight of the possum?" << endl;
  cin >> weight;

  // Computations
  handleLength = (static_cast<float>(stinkFactor) / IDIOTS) * ((3 * lengthOfTail) + weight) + ((30 * stinkFactor) / barometricPressure);
  forkNumber = static_cast<int>(handleLength) / 10;
  
  // Outputs
  cout << "For the following inputs:" << endl;  
  cout << "Weight:                 " << weight << endl;
  cout << "Bar Pressure:           " << barometricPressure << endl; 
  cout << "Stink:                  " << stinkFactor << endl;
  cout << "Tail Length:            " << lengthOfTail << endl; 
  cout << "Handle Length is:       " << handleLength << " and " << endl;
  cout << "Fork Number is:         " << forkNumber << endl; 
    
  return 0;
}
