// Name: CJ Hess
// File: hw3.cpp
// Date: February 11th, 2020
// Instructor: Doris Brown
// Purpose: This program helps determine if the user needs
// to work and what amount of work they need to do
// based on multiple different factors
# include <iostream>
# include <string>
using namespace std;

int main()
{
  // Constants Declarations
  const double HIGH_RAIN_CHECK = 1.5;
  const double LOW_RAIN_CHECK = 0.5;
  const double LOW_GAS_CHECK = 5.0;
  const double HIGH_GAS_CHECK = 10.0;
  // Variable Declarations
  string usersName = "";
  char motivation, isSuperintendentHere;
  bool rainedLastNight = false;
  double rainInInches = 0.0, gallonsOfGas = 0.0;
  int numOfAdults = 0, numOfChildren = 0;
  // Greetings
  cout << "Welcome back user! Let's see if you need to work today." << endl;
  cout << "What is your name user?" << endl;
  cin >> usersName;
  // Decision Branching and Evaluations
  cout << usersName << ", how motivated are you to work today?" << endl;
  cout << "a) an excellent worker" << endl;
  cout << "b) basically good worker" << endl;
  cout << "c) can't get good help no more" << endl;
  cout << "d) don't plan on work from me" << endl;
  cout << "e) elevated slothfulness" << endl;
  cin >> motivation;
  while ((motivation != 'A') && (motivation != 'a') &&
          (motivation != 'B') && (motivation != 'b') &&
          (motivation != 'C') && (motivation != 'c') &&
          (motivation != 'D') && (motivation != 'd') &&
          (motivation != 'E') && (motivation != 'e'))
          {
            cout << "invalid input" << endl;
            cout << usersName << ", how motivated are you to work today?" 
            << endl;
            cout << "a) an excellent worker" << endl;
            cout << "b) basically good worker" << endl;
            cout << "c) can't get good help no more" << endl;
            cout << "d) don't plan on work from me" << endl;
            cout << "e) elevated slothfulness" << endl;
            cin >> motivation;
          }
  if (motivation == 'e' || motivation == 'E') // motivation e branch
    cout << "Stay in bed " << usersName << " and skip work" << endl;
  else if (motivation == 'd' || motivation == 'D') // motivation d branch
  {
    cout << usersName << ", how much did it rain last night?" << endl;
    cin >> rainInInches;
    while (rainInInches < 0.0 || rainInInches > 50.0)
    {
      cout << "Invalid input" << endl;
      cout << usersName << ", how much did it rain last night?" << endl;
      cin >> rainInInches;
    }
    if (rainInInches == 0.0)
      rainedLastNight = false;
    else
      rainedLastNight =true;
    if (rainedLastNight)
      cout << usersName << ", you should hide in the tool shed" << endl;
    else
      cout << usersName << ", you should hide in the hedge" << endl;
  }
  else if (motivation == 'c' || motivation == 'C') // motivation c branch
  {
    cout << usersName << ", how much has it rained?" << endl;
    cin >> rainInInches;
    while (rainInInches < 0.0 && rainInInches > 50.0)
    {
      if (rainInInches < 0.0) // If rain in inches is negative
      {
        cout << "It can't rain negative, do you want to get sued?" << endl;
        cout << usersName << ", how much has it rained?" << endl;
        cin >> rainInInches;
      }
      else if (rainInInches > 50.0) // If rain in inches is very big
      {
        cout << "More than 50 inches! Where is the ark!" << endl;
        cout << usersName << ", how much has it rained?" << endl;
        cin >> rainInInches;
      }
    }
    if (rainInInches <= HIGH_RAIN_CHECK)
      cout << usersName << ", you should lean on a rake" << endl;
    else
      cout << usersName << ", you should lean on a broom" << endl;
  } 
  else if (motivation == 'b' && motivation == 'B') // motivation b branch
  {
    cout << usersName << ", is Superintendent Chalmers present? y/n" << endl;
    cin >> isSuperintendentHere;
    while (isSuperintendentHere != 'y' || isSuperintendentHere != 'n')
    {
      cout << "Invalid Inputs" << endl;
      cout << usersName << ", is Superintendent Chalmers present? y/n" << endl;
      cin >> isSuperintendentHere;
    }
    if (isSuperintendentHere == 'y')
    {
      cout << usersName << ", you should get on your hands and knees and " <<
      "scrub the floor" << endl;
    }
    else if (isSuperintendentHere == 'n')
    {
      cout << usersName << ", how many children are there present?" << endl;
      cin >> numOfChildren;
      while (numOfChildren < 0 || numOfChildren > 100)
      {
        cout << "Invalid Input" << endl;
        cout << usersName << ", how many children are there present?" << endl;
        cin >> numOfChildren;
      }
      cout << usersName << ", how many adults are there present?" << endl;
      cin >> numOfAdults;
      while (numOfAdults < 0 || numOfAdults > 100)
      {
        cout << "Invalid Input" << endl;
        cout << usersName << ", how many adults are there present?" << endl;
        cin >> numOfAdults;
      }
      if (numOfChildren < numOfAdults)
      {
        cout << usersName << ", you should get on your hands and knees and " <<
      "scrub the floor" << endl;
      }
      else
      {
        cout << usersName << ", you should mop the floor." << endl;
      }
    }
  }
  else if (motivation == 'a' || motivation == 'A') // motivation a branch
  {
    cout << usersName << ", how much has it rained?" << endl;
    cin >> rainInInches;
    while (rainInInches < 0.0 || rainInInches > 50.0)
    {
      if (rainInInches < 0.0) // If rain in inches is negative
      {
        cout << "It can't rain negative, do you want to get sued?" << endl;
        cout << usersName << ", how much has it rained?" << endl;
        cin >> rainInInches;
      }
      else if (rainInInches > 50.0) // If rain in inches is very big
      {
        cout << "More than 50 inches! Where is the ark!" << endl;
        cout << usersName << ", how much has it rained?" << endl;
        cin >> rainInInches;
      }
    }
    if (rainInInches == 0)
    {
      rainedLastNight = false;
      cout << usersName << ", how many gallons of gas do you have?" << endl;
      cin >> gallonsOfGas;
      while (gallonsOfGas < 0.0 || gallonsOfGas > 500.0)
      {
        if (gallonsOfGas < 0.0) // If gallons of gas is negative
        {
          cout << "Negative gas? Did the gas go into the pump?" << endl;
          cout << usersName << ", how many gallons of gas do you have?"
          << endl;
          cin >> gallonsOfGas;
        }
        else if (gallonsOfGas > 500.0)
        {
          cout << "You have too much gas, try using some of it." << endl;
          cout << usersName << ", how many gallons of gas do you have?" 
          << endl;
          cin >> gallonsOfGas;
        }
      }
    }
    else 
    {
      cout << usersName << ", how many gallons of gas do you have?" << endl;
      cin >> gallonsOfGas;
      while (gallonsOfGas < 0.0 || gallonsOfGas > 500.0)
      {
        if (gallonsOfGas < 0.0) // If gallons of gas is negative
        {
          cout << "Negative gas? Did the gas go into the pump?";
          cout << usersName << ", how many gallons of gas do you have?" 
          << endl;
          cin >> gallonsOfGas;
        }
        else if (gallonsOfGas > 500.0) // If gallons of gas is big
        {
          cout << "You have too much gas, try using some of it.";
          cout << usersName << ", how many gallons of gas do you have?" 
          << endl;
          cin >> gallonsOfGas;
        }
      }
    }
    if ((gallonsOfGas >= LOW_GAS_CHECK && gallonsOfGas <= HIGH_GAS_CHECK) && 
    (rainInInches < LOW_RAIN_CHECK))
    {
      cout << usersName << ", you should mow the grass." << endl;
    }
    else if (gallonsOfGas > HIGH_GAS_CHECK && rainInInches < LOW_RAIN_CHECK)
    {
      cout << usersName << ", you should get on the tractor and do laps " <<
      "around the school" << endl;
    }
    else if (gallonsOfGas < LOW_GAS_CHECK && rainInInches < LOW_RAIN_CHECK)
    {
      cout << usersName << ", you should go get gas" << endl;
    }
    else if (rainInInches > LOW_RAIN_CHECK)
    {
      if (gallonsOfGas < 5)
      {
        cout << usersName << ", you should burn old text books from the 1940s"
        << endl;
      }
      else
      {
        cout << usersName << ", you should use that gas to clean the bathrooms"
        << endl;
      }
    }
  }
  else
  {
    cout << usersName << ", you should a write c++ program" << endl;
  }
  cout << "Thank you for using the work needed evaluation." << endl;
  // Return Value!
  return 0;
}
