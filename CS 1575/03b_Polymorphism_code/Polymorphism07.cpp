/**
  Destructors are chained automatically for standard inheritance.
  Note, this is not polymorphic upcasting with a pointer of the parent class type pointing to the child object.
 **/

#include <iostream>

using std::cout;
using std::endl;

class Base
{
    public:
        virtual ~Base()
        {
            cout << "Base Destructor" << endl;
        }
};


class Derived: public Base
{
    public:
        ~Derived()
        {
            cout<< "Derived Destructor" << endl;
        }
};

int main()
{
    Base *b = new Base;
    Derived *d = new Derived;

    // delete a regular dynamic base object?
    delete b; // ??

    // delete a regular dynamic derived object?
    delete d; // ??

    return 0;
}

// Ask: Is the order the same as constructors, or reversed?
// back to pres
