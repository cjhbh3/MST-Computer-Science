// Name: CJ Hess
// Date: February 25th, 2020
// File: lab6.cpp
// Purpose: The purpose of this program is too simulate
// battles between Dragons and Hunting Ships. 
// It will output turn by turn attacks or misses.

#include <iostream>
#include <string>
#include <cstdlib>
using namespace std;

struct hunterShip 
{
    int m_ShipHealth;
    int m_CrewSize;
    bool m_Captured;
};

struct dragonRider 
{
    string m_RiderName;
    string m_DragonName;
    int m_Health;
    bool m_Captured;
};

int main()
{
    // Seed RNG
    srand(time(NULL));
    // Variables
    const int HUNTER_SIZE = 7;
    const int DRAGON_SIZE = 5;
    hunterShip huntingShips[HUNTER_SIZE];
    dragonRider dragonRiders[DRAGON_SIZE];
    bool allShipsCaptured = false;
    bool allDragonsCaptured = false;
    int roundNumber = 1;
    int numHunter = 0;
    for (int i = 0; i < DRAGON_SIZE; i++)
    {
        dragonRider newDragon;
        cout << "What is the rider name?" << endl;
        cin >> newDragon.m_RiderName;
        cout << "What is the dragon name?" << endl;
        cin >> newDragon.m_DragonName;
        newDragon.m_Health = (15 + rand() % (6));
        newDragon.m_Captured = false;
        dragonRiders[i] = newDragon;
    }

    for (int i = 0; i < HUNTER_SIZE; i++)
    {
        hunterShip newHunterShip;
        newHunterShip.m_ShipHealth = (30 +rand() % (11));
        newHunterShip.m_CrewSize = (10 + rand() % (6));
        newHunterShip.m_Captured = false;
        huntingShips[i] = newHunterShip;
    }

    while (!allShipsCaptured && !allDragonsCaptured)
    {  
        cout << "Round " << roundNumber << endl;
        if (huntingShips[0].m_ShipHealth > 0 || huntingShips[0].m_CrewSize > 0)
        {
            for (dragonRider dragon : dragonRiders)
            {
                if (dragon.m_Captured == false)
                {
                    if ((1+rand()%(10)) <= 7)
                    {
                        cout << dragon.m_DragonName << " lands a hit." << endl;
                        huntingShips[0].m_ShipHealth -= ((5+rand()%(6)));
                        if ((1+rand()%(10)) <= 3)
                        {
                            huntingShips[0].m_CrewSize -= (2+rand()%(2));
                        }
                    }
                    else 
                    {
                        cout << dragon.m_DragonName << " missed." << endl;
                    }
                }
            }
            if (huntingShips[0].m_ShipHealth <= 0 || 
            huntingShips[0].m_CrewSize <= 0)
            {
                huntingShips[0].m_Captured = true;
            }
        }
        else if (dragonRiders[0].m_Health > 0)
        {
            for (hunterShip hunter : huntingShips)
            {
                if (hunter.m_Captured == false)
                {
                    if ((1+rand()%(10)) <= 4)
                    {
                        cout << dragonRiders[0].m_DragonName << " has been hit." 
                        << endl;
                        dragonRiders[0].m_Health -= (4+rand()%(2));
                    }
                    else 
                    {
                        cout << "Hunter missed." << endl;
                    }
                } 
            }
            if (dragonRiders[0].m_Health <= 0)
            {
                dragonRiders[0].m_Captured = true;
            }
        }

        else if (huntingShips[1].m_ShipHealth > 0 || huntingShips[1].m_CrewSize > 0)
        {
            for (dragonRider dragon : dragonRiders)
            {
                if (dragon.m_Captured == false)
                {
                    if ((1+rand()%(10)) <= 7)
                    {
                        cout << dragon.m_DragonName << " lands a hit." << endl;
                        huntingShips[1].m_ShipHealth -= ((5+rand()%(6)));
                        if ((1+rand()%(10)) <= 3)
                        {
                            huntingShips[1].m_CrewSize -= (2+rand()%(2));
                        }
                    }
                    else 
                    {
                        cout << dragon.m_DragonName << " missed." << endl;
                    }
                }
            }
            if (huntingShips[1].m_ShipHealth <= 0 || 
            huntingShips[1].m_CrewSize <= 0)
            {
                huntingShips[1].m_Captured = true;
            }
        }
        else if (dragonRiders[1].m_Health > 0)
        {
            for (hunterShip hunter : huntingShips)
            {
                if (hunter.m_Captured == false)
                {
                    if ((1+rand()%(10)) <= 4)
                    {
                        cout << dragonRiders[1].m_DragonName << " has been hit." 
                        << endl;
                        dragonRiders[1].m_Health -= (4+rand()%(2));
                    }
                    else 
                    {
                        cout << "Hunter missed." << endl;
                    }
                }
            }
            if (dragonRiders[1].m_Health <= 0)
            {
                dragonRiders[1].m_Captured = true;
            }
        }

        else if (huntingShips[2].m_ShipHealth > 0 || huntingShips[2].m_CrewSize > 0)
        {
            for (dragonRider dragon : dragonRiders)
            {
                if (dragon.m_Captured == false)
                {
                    if ((1+rand()%(10)) <= 7)
                    {
                        cout << dragon.m_DragonName << " lands a hit." << endl;
                        huntingShips[2].m_ShipHealth -= ((5+rand()%(6)));
                        if ((1+rand()%(10)) <= 3)
                        {
                            huntingShips[2].m_CrewSize -= (2+rand()%(2));
                        }
                    }
                    else 
                    {
                        cout << dragon.m_DragonName << " missed." << endl;
                    }
                }
            }
            if (huntingShips[2].m_ShipHealth <= 0 || 
            huntingShips[2].m_CrewSize <= 0)
            {
                huntingShips[2].m_Captured = true;
            }
        }
        else if (dragonRiders[2].m_Health > 0)
        {
            for (hunterShip hunter : huntingShips)
            {
                if (hunter.m_Captured == false)
                {
                    if ((1+rand()%(10)) <= 4)
                    {
                        cout << dragonRiders[2].m_DragonName << " has been hit." 
                        << endl;
                        dragonRiders[2].m_Health -= (4+rand()%(2));
                    }
                    else 
                    {
                        cout << "Hunter missed." << endl;
                    }
                } 
            }
            if (dragonRiders[2].m_Health <= 0)
            {
                dragonRiders[2].m_Captured = true;
            }
        }

        else if (huntingShips[3].m_ShipHealth > 0 || huntingShips[3].m_CrewSize > 0)
        {
            for (dragonRider dragon : dragonRiders)
            {
                if (dragon.m_Captured == false)
                {
                    if ((1+rand()%(10)) <= 7)
                    {
                        cout << dragon.m_DragonName << " lands a hit." << endl;
                        huntingShips[3].m_ShipHealth -= ((5+rand()%(6)));
                        if ((1+rand()%(10)) <= 3)
                        {
                            huntingShips[3].m_CrewSize -= (2+rand()%(2));
                        }
                    }
                    else 
                    {
                        cout << dragon.m_DragonName << " missed." << endl;
                    }
                }
            }
            if (huntingShips[3].m_ShipHealth <= 0 || 
            huntingShips[2].m_CrewSize <= 0)
            {
                huntingShips[3].m_Captured = true;
            }
        }
        else if (dragonRiders[3].m_Health > 0)
        {
            for (hunterShip hunter : huntingShips)
            {
                if (hunter.m_Captured == false)
                {
                    if ((1+rand()%(10)) <= 4)
                    {
                        cout << dragonRiders[3].m_DragonName << " has been hit." 
                        << endl;
                        dragonRiders[3].m_Health -= (4+rand()%(2));
                    }
                    else 
                    {
                        cout << "Hunter missed." << endl;
                    }
                } 
            }
            if (dragonRiders[3].m_Health <= 0)
            {
                dragonRiders[3].m_Captured = true;
            }
        }

        else if (huntingShips[4].m_ShipHealth > 0 || huntingShips[4].m_CrewSize > 0)
        {
            for (dragonRider dragon : dragonRiders)
            {
                if (dragon.m_Captured == false)
                {
                    if ((1+rand()%(10)) <= 7)
                    {
                        cout << dragon.m_DragonName << " lands a hit." << endl;
                        huntingShips[4].m_ShipHealth -= ((5+rand()%(6)));
                        if ((1+rand()%(10)) <= 3)
                        {
                            huntingShips[4].m_CrewSize -= (2+rand()%(2));
                        }
                    }
                    else 
                    {
                        cout << dragon.m_DragonName << " missed." << endl;
                    }
                }
            }
            if (huntingShips[4].m_ShipHealth <= 0 || 
            huntingShips[4].m_CrewSize <= 0)
            {
                huntingShips[4].m_Captured = true;
            }
        }
        else if (dragonRiders[4].m_Health > 0)
        {
            for (hunterShip hunter : huntingShips)
            {
                if (hunter.m_Captured == false)
                {
                    if ((1+rand()%(10)) <= 4)
                    {
                        cout << dragonRiders[4].m_DragonName << " has been hit." 
                        << endl;
                        dragonRiders[4].m_Health -= (4+rand()%(2));
                    }
                    else 
                    {
                        cout << "Hunter missed." << endl;
                    }
                } 
            }
            if (dragonRiders[4].m_Health <= 0)
            {
                dragonRiders[4].m_Captured = true;
            }
        }

        else if (huntingShips[5].m_ShipHealth > 0 || huntingShips[5].m_CrewSize > 0)
        {
            for (dragonRider dragon : dragonRiders)
            {
                if (dragon.m_Captured == false)
                {
                    if ((1+rand()%(10)) <= 7)
                    {
                        cout << dragon.m_DragonName << " lands a hit." << endl;
                        huntingShips[5].m_ShipHealth -= ((5+rand()%(6)));
                        if ((1+rand()%(10)) <= 3)
                        {
                            huntingShips[5].m_CrewSize -= (2+rand()%(2));
                        }
                    }
                    else 
                    {
                        cout << dragon.m_DragonName << " missed." << endl;
                    }
                }
                
            }
            if (huntingShips[5].m_ShipHealth <= 0 || 
            huntingShips[5].m_CrewSize <= 0)
            {
                huntingShips[5].m_Captured = true;
            }
        }

        else if (huntingShips[6].m_ShipHealth > 0 || huntingShips[6].m_CrewSize > 0)
        {
            for (dragonRider dragon : dragonRiders)
            {
                if (dragon.m_Captured == false)
                {
                    if ((1+rand()%(10)) <= 7)
                    {
                        cout << dragon.m_DragonName << " lands a hit." << endl;
                        huntingShips[6].m_ShipHealth -= ((5+rand()%(6)));
                        if ((1+rand()%(10)) <= 3)
                        {
                            huntingShips[6].m_CrewSize -= (2+rand()%(2));
                        }
                    }
                    else 
                    {
                        cout << dragon.m_DragonName << " missed." << endl;
                    }
                }
            }
            if (huntingShips[6].m_ShipHealth <= 0 || 
            huntingShips[6].m_CrewSize <= 0)
            {
                huntingShips[6].m_Captured = true;
            }
        }
        allDragonsCaptured = (dragonRiders[0].m_Captured && 
        dragonRiders[1].m_Captured && dragonRiders[2].m_Captured &&
        dragonRiders[3].m_Captured && dragonRiders[4].m_Captured);
        allShipsCaptured = (huntingShips[0].m_Captured && 
        huntingShips[1].m_Captured && huntingShips[2].m_Captured &&
        huntingShips[3].m_Captured && huntingShips[4].m_Captured &&
        huntingShips[5].m_Captured && huntingShips[6].m_Captured);
        roundNumber ++;
    }
    if (!allDragonsCaptured)
    {
        cout << "Dragons win!" << endl;
    }
    else if (!allShipsCaptured)
    {
        cout << "Hunters win!" << endl;
    }
    for (dragonRider dragon : dragonRiders)
    {
        if (dragon.m_Captured == false)
        {
            cout << dragon.m_DragonName << " Health:" << endl;
            cout << dragon.m_Health << endl;
        }
    }
    for (hunterShip hunter : huntingShips)
    {
        
        if (hunter.m_Captured == false)
        {
            numHunter ++;
            cout << "Hunter " << numHunter << " Health:" << endl;
            cout << hunter.m_ShipHealth << endl;
        }
        cout << endl;
    }
    return 0;
}