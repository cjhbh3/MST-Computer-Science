/**
  What happens to a virtual function not re-defined in derived?
 **/

#include <iostream>

using std::cout;
using std::endl;

class Base
{
    public:
        virtual void baseFunc()
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
    Base* b;       //Base class pointer
    Derived d;     //Derived class object
    b = &d;

    // The standard member function, not ever overridden
    d.derivedFunc();   //??

    // Can you still call a parent's virtual function in the child class?
    d.baseFunc();   //?? Still virtual, to what consequence?

    // Pointer of base type points to derived object, calling base function which has not been overridden
    b->baseFunc();     //Early Binding Occurs ??

    b->derivedFunc();     //Early Binding Occurs ??

    return 0;
}

// back to pres
