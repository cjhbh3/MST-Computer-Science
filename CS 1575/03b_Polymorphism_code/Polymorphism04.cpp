/**
  Virtual functions in the base class for polymorphism.
 **/

#include <iostream>

using std::cout;
using std::endl;

class Base
{
    public:
        virtual void show()
        {
            cout << "Base class" << endl;
        }
};

class Derived1: public Base
{
    public:
        void show() override
        {
            cout << "Derived Class 1" << endl;
        }
};

class Derived2: public Base
{
    public:
        void show() override 
        {
            cout << "Derived Class 2" << endl;
        }
};

int main()
{
    Base *b;       //Base class pointer
    Derived1 d1;     //Derived class object
    b = &d1;

    // Standard overriding
    d1.show();  // ??

    // pointer of base type pointing to derived object, calling overriden function?
    b->show();     //Early Binding Occurs ??

    // b gets assigned to another devired object
    Derived2 d2;     //Derived class object
    b = &d2;

    d2.show();  // ??
    b->show();     //Early Binding Occurs ??

    // Can we still call a virtual function from a regular base object?
    Base bObj;
    bObj.show();

    // What happens to those show functions in the derived class?
    // Is it accessible via both the base pointer and the derived object?
    b->Base::show();
    d1.Base::show();


    return 0;
}
