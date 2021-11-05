// Name: CJ Hess
// Date: February 18th, 2020
// File: lab5.cpp
// Purpose: The purpose of this program is to find a suitable island,
// build facilities on the island, and finally annouce the island is 
// complete.
# include <iostream>
# include <cstdlib>
using namespace std;

// Random Num Gen: (min + rand() % (max-min+1)
int main()
{
  // Variable Declarations
  int mainMenuChoice = 0;
  int buildingMenuChoice = 0;
  int islandOption = 0;
  int facilityBuilt = 0;
  bool islandAvailable = false;
  bool housingBuilt = false;
  bool trainingBuilt = false;
  bool stablesBuilt = false;
  bool travelBuilt = false;
  bool defensesBuilt = false;
  bool islandFinish = false;
  bool islandDone = false;

  // Seed Random
  srand(time(NULL));
  // Greeting
  cout << "Welcome weary traveler. Lets find land and build a base" << endl;
  // Menu
  while (!islandDone)
  {
    cout << "Please select an option below: " << endl;
    cout << "1. Search for island" << endl;
    cout << "2. Build on the island" << endl;
    cout << "3. Complete the island" << endl;
    cin >> mainMenuChoice;
    while (mainMenuChoice != 1 && mainMenuChoice != 2 && mainMenuChoice != 3)
    {
      cout << "Invalid Input" << endl;
      cin >> mainMenuChoice;
    }
    if (mainMenuChoice == 1)
    {
      islandOption = 1 + rand() % (4);
      switch (islandOption)
      {
        case 1:
          cout << "The island is uninhabited, but dangerous and thus unusable." 
          << endl;
          break;
        case 2:
          cout << "The island is inhabited by aggressive dragons" << 
          " and thus not usable." << endl;
          break;
        case 3:
          cout << "The island is a base for dragon trappers and unusable." 
          << endl;
          break;
        case 4:
          cout << "The island has just the right conditions that a base can " 
          << "be built on it." << endl;
          islandAvailable = true;
          break;
      }
    }
    else if (mainMenuChoice == 2)
    {
      if (islandAvailable)
      {
        while (!islandFinish)
        {
          cout << "Please select an option below: " << endl;
          cout << "1. Build housing" << endl;
          cout << "2. Build training arena" << endl;
          cout << "3. Build stables" << endl;
          cout << "4. Build travel systems" << endl;
          cout << "5. Build defenses" << endl;
          cin >> buildingMenuChoice;
          while (buildingMenuChoice != 1 && buildingMenuChoice != 2 && 
          buildingMenuChoice != 3 && buildingMenuChoice != 4 && 
          buildingMenuChoice != 5)
          {
            cout << "Invalid Input" << endl;
            cin >> buildingMenuChoice;
          }
          if (buildingMenuChoice == 1)
          {
            facilityBuilt = 1+rand()%(2);
            switch (facilityBuilt)
            {
              case 1:
                cout << "Housing facility is complete, on to the next!" 
                << endl;
                housingBuilt = true;
                break;
              case 2: 
                cout << "Housing facility is mostly complete, please try again" 
                << endl;
                break;
            }
          }
          else if (buildingMenuChoice == 2)
          {
            facilityBuilt = 1+rand()%(2);
            switch (facilityBuilt)
            {
              case 1:
                cout << "Training facility is complete, on to the next!" 
                << endl;
                trainingBuilt = true;
                break;
              case 2: 
                cout << "Training facility is mostly complete, please try "
                << "again" << endl;
                break;
            }
          }
          else if (buildingMenuChoice == 3)
          {
            facilityBuilt = 1+rand()%(2);
            switch (facilityBuilt)
            {
              case 1:
                cout << "Stable facility is complete, on to the next!" 
                << endl;
                stablesBuilt = true;
                break;
              case 2: 
                cout << "Stable facility is mostly complete, please try "
                << "again" << endl;
                break;
            }
          }
          else if (buildingMenuChoice == 4)
          {
            facilityBuilt = 1+rand()%(2);
            switch (facilityBuilt)
            {
              case 1:
                cout << "Travel facility is complete, on to the next!" 
                << endl;
                travelBuilt = true;
                break;
              case 2: 
                cout << "Travel facility is mostly complete, please try "
                << "again" << endl;
                break;
            }
          }
          else if (buildingMenuChoice == 5)
          {
            facilityBuilt = 1+rand()%(2);
            switch (facilityBuilt)
            {
              case 1:
                cout << "Defense facility is complete, on to the next!" 
                << endl;
                defensesBuilt = true;
                break;
              case 2: 
                cout << "Defense facility is mostly complete, please try "
                << "again" << endl;
                break;
            }
          }
          islandFinish = (housingBuilt && trainingBuilt && stablesBuilt 
          && travelBuilt && defensesBuilt);
        }
      }
      else
      {
        cout << "Island not available. Please find an island." << endl;
      }
    }
    else if (mainMenuChoice == 3)
    {
      if (islandAvailable && islandFinish)
      {
        cout << "The edge is finished, time to explore!" << endl;
        islandDone = true;
      }
    }
  }
  return 0;
}
