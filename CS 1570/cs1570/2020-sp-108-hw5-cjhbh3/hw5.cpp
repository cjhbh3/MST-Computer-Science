// Name: CJ Hess
// Date: February 25th, 2020
// File: hw5.cpp
// Purpose:

# include <iostream>
# include <string>
using namespace std;

struct locker { // Declared a variable type called locker
  // Attributes: locker number, number of texts, money, student name
  // and if the locker is occupied
  bool m_Occupied;
  double m_Money;
  int m_LockerNumber;
  int m_NumOfTextbooks;
  string m_StudentLastName;
};

int main()
{
  // Variable declarations
  const char MENU_CHOICE_A = 'a';
  const char MENU_CHOICE_P = 'p';
  const char MENU_CHOICE_O = 'o';
  const char MENU_CHOICE_D = 'd';
  const char MENU_CHOICE_Q = 'q';
  const char MENU_CHOICE_1 = '1';
  const char MENU_CHOICE_2 = '2';
  const char MENU_CHOICE_3 = '3';
  const char MENU_CHOICE_4 = '4';
  const char MENU_CHOICE_5 = '5';
  const double MONEY_MAX = 150.00;
  const double MONEY_MIN = 0.00;
  const int SIZE = 101;
  bool quitMenu = false;
  char menuChoice;
  double sumOfMoney = 0.0;  
  int lockerNumber;
  int lockersOccupied;
  locker lockerList[SIZE];
  locker newLocker;
  locker currentLocker;
  // Greeting
  cout << "Welcome to the locker tracker, Groundskeeper!" << endl;
  // Format Adjustment
  cout.setf(ios::fixed);
  cout.setf(ios::showpoint);
  cout.precision(2);
  // Locker Occupied Count
  lockersOccupied = 0;
  for (locker current : lockerList)
  {
    if (current.m_Occupied)
    {
      lockersOccupied++;
    }
  }
  // Menu
  cout << "Locker tracker" << endl;
  cout << "--------------" << endl;
  cout << "1. Add a locker" << endl;
  cout << "2. Print contents of a locker" << endl;
  cout << "3. Output all locker contents" << endl;
  cout << "4. Delete a locker" << endl;
  cout << "5. Quit" << endl << endl;
  cout << "There are " << lockersOccupied << " occupied lockers" << endl
  << endl;
  cout << "Pick an option from above" << endl;
  cin >> menuChoice;
  while (menuChoice != MENU_CHOICE_A && menuChoice != MENU_CHOICE_P &&
  menuChoice != MENU_CHOICE_O && menuChoice != MENU_CHOICE_D &&
  menuChoice != MENU_CHOICE_Q && menuChoice != MENU_CHOICE_1 &&
  menuChoice != MENU_CHOICE_2 && menuChoice != MENU_CHOICE_3 &&
  menuChoice != MENU_CHOICE_4 && menuChoice != MENU_CHOICE_5)
  {
    cout << "Locker tracker" << endl;
    cout << "--------------" << endl;
    cout << "1. Add a locker" << endl;
    cout << "2. Print contents of a locker" << endl;
    cout << "3. Output all locker contents" << endl;
    cout << "4. Delete a locker" << endl;
    cout << "5. Quit" << endl;
    cin >> menuChoice;
    cout << "There are " << lockersOccupied << " occupied lockers" << endl
    << endl;
    cout << "Pick an option from above" << endl;
  }
  while (!quitMenu)
  {
    if (menuChoice == MENU_CHOICE_A || menuChoice == MENU_CHOICE_1) 
    { // Add a locker: prompt for locker number, name, textbooks, and money
      cout << "What is the locker number?" << endl;
      cin >> newLocker.m_LockerNumber;
      while (newLocker.m_LockerNumber < 101 || newLocker.m_LockerNumber > 201)
      { // Input checking: if it is below 101 and above 201, re-prompt
        cout << "Invalid Input" << endl;
        cout << "What is the locker number?" << endl;
        cin >> newLocker.m_LockerNumber;
      }
      cout << "What is the locker name?" << endl;
      cin >> newLocker.m_StudentLastName;
      cout << "How many textbooks are there?" << endl;
      cin >> newLocker.m_NumOfTextbooks;
      while (newLocker.m_NumOfTextbooks < 0)
      { // Input checking: if number of textbooks is negative, re-prompt
        cout << "Invalid Input" << endl;
        cout << "How many textbooks are there?" << endl;
        cin >> newLocker.m_NumOfTextbooks;
      }
      cout << "How much money is in there?" << endl;
      cin >> newLocker.m_Money;
      while (newLocker.m_Money < 0.0)
      { // Input checking: if the money is negative, re-prompt
        cout << "How much money is in there?" << endl;
        cin >> newLocker.m_Money;
      }
      sumOfMoney += newLocker.m_Money;
      newLocker.m_Occupied = true;
      lockerList[newLocker.m_LockerNumber-101] = newLocker; // Add locker to list
    } 
    else if (menuChoice == MENU_CHOICE_P || menuChoice == MENU_CHOICE_2)
    {
      cout << "What is the locker number?" << endl;
      cin >> lockerNumber;
      while (lockerNumber < 101 || lockerNumber > 201)
      { // Input checking: if it is below 101 and above 201, re-prompt
        cout << "Invalid Input" << endl;
        cout << "What is the locker number?" << endl;
        cin >> lockerNumber;
      }
      lockerNumber = lockerNumber - 101; // Adjust for indexing
      if (lockerList[lockerNumber].m_Occupied)
      {
        cout << "The locker is owned by: " << 
        lockerList[lockerNumber].m_StudentLastName << endl;
        cout << "The locker has " << lockerList[lockerNumber].m_NumOfTextbooks
        << " textbooks" << endl;
        cout << "The locker has $" << lockerList[lockerNumber].m_Money <<
        " in money." << endl;
      }
      else
      {
        cout << "This locker is unoccupied." << endl;
      }
    }/*
    else if (menuChoice == MENU_CHOICE_O || menuChoice == MENU_CHOICE_3)
    {

    }
    else if (menuChoice == MENU_CHOICE_D || menuChoice == MENU_CHOICE_4)
    {

    }*/
    else if (menuChoice == MENU_CHOICE_Q || menuChoice == MENU_CHOICE_5)
    {
      quitMenu = true;
    }/*
    else 
    {

    }*/
    lockersOccupied = 0;
    if (sumOfMoney > MONEY_MAX)
    {
      for (locker current : lockerList)
      {
        if (current.m_Occupied)
        {
          current.m_Money = MONEY_MIN;
          lockersOccupied++;
        }
      }
      sumOfMoney = MONEY_MIN;
    }
    if (!quitMenu)
    {
      cout << "Locker tracker" << endl;
      cout << "--------------" << endl;
      cout << "1. Add a locker" << endl;
      cout << "2. Print contents of a locker" << endl;
      cout << "3. Output all locker contents" << endl;
      cout << "4. Delete a locker" << endl;
      cout << "5. Quit" << endl;
      cout << "There are " << lockersOccupied << " occupied lockers" << endl
      << endl;
      cout << "Pick an option from above" << endl;
      cin >> menuChoice;
      while (menuChoice != MENU_CHOICE_A && menuChoice != MENU_CHOICE_P &&
      menuChoice != MENU_CHOICE_O && menuChoice != MENU_CHOICE_D &&
      menuChoice != MENU_CHOICE_Q && menuChoice != MENU_CHOICE_1 &&
      menuChoice != MENU_CHOICE_2 && menuChoice != MENU_CHOICE_3 &&
      menuChoice != MENU_CHOICE_4 && menuChoice != MENU_CHOICE_5)
      {
        cout << "Locker tracker" << endl;
        cout << "--------------" << endl;
        cout << "1. Add a locker" << endl;
        cout << "2. Print contents of a locker" << endl;
        cout << "3. Output all locker contents" << endl;
        cout << "4. Delete a locker" << endl;
        cout << "5. Quit" << endl;
        cin >> menuChoice;
      }
    }
  }
  return 0;
}