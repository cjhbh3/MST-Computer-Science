// Name: CJ Hess
// Date: March 17th, 2020
// File: header.cpp
// Purpose: This file contains all the 
// function bodies

#include "header.h"


void averages(const int numArray[], double averageArray[], const int size)
{
  double average = 0.0;
  for (int i = 0; i < size; i++)
  {
    if (i==0)
    {
      average = 0.0;
    }
    else 
    {
      average = (numArray[i] + numArray[i-1]) / 2.0;
    }
    averageArray[i] = average;
  }
  return;
}

void sort(double array[], const int size)
{
  for (int i = 0; i < size; i++)
  {
    for (int j = 0; j < size; j++)
    {
      if (array[i] < array[j])
      {
        double temp = array[i];
        array[i] = array[j];
        array[j] = temp;
      }
    }
  }
  return;
}

double median(const double array[], const int size)
{
  double medianNum;
  int middle = size / 2;
  if (size % 2 == 0)
  {
    medianNum = (array[middle-1] + array[middle]) / 2;
  }
  else
  {
    medianNum = array[middle];
  }
  return medianNum;
}

double mode(const double array[], const int size)
{
  double mode;
  double currentNum;
  int count = 0;
  int greatest = 0;
  for (int i = 0; i < size; i++)
  {
    currentNum = array[i];
    for (int j = 0; j < size; j++)
    {
      if (i!=j)
      {
        if (currentNum == array[j])
        {
          count++;
        }
      }
    }
    if (count > greatest)
    {
      greatest = count;
      mode = currentNum;
    }
    count = 0;
  }
  return mode;
}