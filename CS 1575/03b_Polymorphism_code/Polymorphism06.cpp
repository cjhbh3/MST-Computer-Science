/**
  Pure virtual functions to make an abstract class
 **/

#include <iostream>

using std::cout;
using std::endl;

class Base          //Abstract base class
{
    public:
        virtual void show() = 0;            //Pure Virtual Function
};

//void Base::show(){}

class Derived: public Base
{
    public:
        void show()
        {
            cout << "Implementation of virtual function in derived class" << endl;
        }
};

int main()
{
    // Can we make a base object?
    //Base obj;       // ??

    // Base pointer to a derived object
    Base *b;
    Derived d;
    b = &d;

    // Stanard overriding even though we used pure virtual?
    d.show();

    // Upcasting with overriding
    b->show();

    // What if we pair this with the commented scoped definition above?
    // b->Base::show();

    return 0;
}

// back to pres
