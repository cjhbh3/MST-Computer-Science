/**
  Upcasting with a pointer to the base class.
  Note the functions below are named differently (no overriding).
 **/

#include <iostream>

using std::cout;
using std::endl;

class Base
{
    public:
        void baseFunc()
        {
            cout << "Base class" << endl;
        }
};

class Derived: public Base
{
    public:
        void derivedFunc()
        {
            cout << "Derived Class" << endl;
        }
};

int main()
{
    Base *b;       //Base class pointer
    Derived d;     //Derived class object
    b = &d;

    // Standard member
    d.derivedFunc();  // ??

    // Stardand inherited member
    d.baseFunc();

    // Pointer of a base type pointing to a derived object, calling a base function
    b->baseFunc();     //Early Binding Occurs
    (*b).baseFunc();
    // Pointer of a base type pointing to a derived object, calling a derived function
    //b->derivedFunc();    //?? Error

    return 0;
}

// back to pres
