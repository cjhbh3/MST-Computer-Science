// Name: CJ Hess
// Date: February 11th, 2020
// File: lab4.cpp
// Purpose: The purpose of this code is to track the feeding of dragons
// This is accomplished by decrementing the rider's food amount and
// incrementing the food amount of each dragon.

# include <iostream>
using namespace std;
int main()
{
  // Variables and Constants
  const int CARRY_LIMIT = 10;
  const int FEEDING_AMOUNT = 10;
  const int FEEDING_GOAL = 100;
  int hiccupValue = 70;
  int astridValue = 60;
  int snotloutValue = 40;
  int fishlegsValue = 50;
  int rufnutTufnutValue = 20;
  int toothlessValue = 0;
  int stormflyValue = 0;
  int hookfangValue = 0;
  int meatlugValue = 0;
  int barfBelchValue = 0;
  bool allDragonsFed = false;
  
  // Computations: the loop contains loops for each dragon that
  // feeds the dragon and take away food from the rider.
  while(!allDragonsFed)
  {
    while(toothlessValue < FEEDING_GOAL)
    {
      if(hiccupValue > 0)
      {
        toothlessValue += FEEDING_AMOUNT;
        hiccupValue -= FEEDING_AMOUNT;
      }
      else if (hiccupValue == 0) 
      {
        hiccupValue += CARRY_LIMIT;
      }
    }
    cout << "Toothless is all full" << endl;

    while(stormflyValue < FEEDING_GOAL)
    {
      if(astridValue > 0)
      {
        stormflyValue += FEEDING_AMOUNT;
        astridValue -= FEEDING_AMOUNT;
      }
      else if (hiccupValue == 0) 
      {
        astridValue += CARRY_LIMIT;
      }
    }
    cout << "Stormyfly is all full" << endl;

    while(hookfangValue < FEEDING_GOAL)
    {
      if(snotloutValue > 0)
      {
        hookfangValue += FEEDING_AMOUNT;
        snotloutValue -= FEEDING_AMOUNT;
      }
      else if (snotloutValue == 0) 
      {
        snotloutValue += CARRY_LIMIT;
      }
    }
    cout << "Hookfang is all full" << endl;

    while(meatlugValue < FEEDING_GOAL)
    {
      if(fishlegsValue > 0)
      {
        meatlugValue += FEEDING_AMOUNT;
        fishlegsValue -= FEEDING_AMOUNT;
      }
      else if (fishlegsValue == 0) 
      {
        fishlegsValue += CARRY_LIMIT;
      }
    }
    cout << "Meatlug is all full" << endl;

    while(barfBelchValue < FEEDING_GOAL)
    {
      if(rufnutTufnutValue > 0)
      {
        barfBelchValue += FEEDING_AMOUNT;
        rufnutTufnutValue -= FEEDING_AMOUNT;
      }
      else if (rufnutTufnutValue == 0) 
      {
        rufnutTufnutValue += CARRY_LIMIT;
      }
    }
    cout << "Barf and Belch is all full" << endl;

    allDragonsFed = ((toothlessValue>=FEEDING_GOAL) && (stormflyValue>=FEEDING_GOAL) && 
    (hookfangValue>=FEEDING_GOAL) && (meatlugValue>=FEEDING_GOAL) && (barfBelchValue>=FEEDING_GOAL));
  }
  // Output
  cout << "Feeding time is over" << endl;
  
  return 0;
}
