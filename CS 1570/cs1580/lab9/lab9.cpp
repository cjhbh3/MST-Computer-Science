// Name: CJ Hess
// Date: March 17th, 2020
// File: lab9.cpp
// Purpose: This program takes input from a file and
// creates an array of averages, computes the median,
// and mode and outputs it to another file

#include "header.h"

int main()
{
  // Variable Declarations
  ifstream in;
  ofstream out;
  const int ARRAY_SIZE = 10;
  int numArray[ARRAY_SIZE];
  double averageArray[ARRAY_SIZE];
  double medianNum;
  double modeNum;
  // opening files
  in.open("input.txt");
  out.open("output.txt");
  for (int i = 0; i < ARRAY_SIZE; i++)
  {
    in>>numArray[i];
  }
  averages(numArray, averageArray, ARRAY_SIZE);
  sort(averageArray, ARRAY_SIZE);
  medianNum = median(averageArray, ARRAY_SIZE);
  modeNum = mode(averageArray, ARRAY_SIZE);
  for (int i = 0; i < ARRAY_SIZE; i++)
  {
    out << averageArray[i] << " ";
  }
  out << endl;
  out <<  medianNum << " " << modeNum << endl;
  in.close();
  return 0;
}