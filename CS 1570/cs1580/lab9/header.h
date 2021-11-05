// Name: CJ Hess
// Date: March 17th, 2020
// File: header.h
// Purpose: This file contains all the 
// function prototypes

#ifndef HEADER_H
#define HEADER_H

#include <fstream>
using namespace std;

// Function Description: This function will fill averageArray with the averages
// of each number with the previous number in numArray
// Precondition: numArray must be filled and same size as size
// Postcondition: Will fill averageArray with the averages of each number and
// the previous number
void averages(const int numArray[], double averageArray[], const int size);

// Function Description: This function will sort the array in ascending order
// Precondition: array must be filled and same size as size
// Postcondition: The array will be sorted in ascending order
void sort(double array[], const int size);

// Function Description: This function will find the median of the array
// Precondition: array must be filled, same size as size, and sorted
// Postcondition: Will return the median of the array
double median(const double array[], const int size);

// Function Description: This function will find the mode of the array
// Precondition: array must be filled, same size as size
// Postcondition: Will return the mode of the array
double mode(const double array[], const int size);

#endif