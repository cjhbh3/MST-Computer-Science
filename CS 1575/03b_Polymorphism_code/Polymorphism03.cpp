/**
  Overriding combined with upcasting the "wrong" way
 **/

#include <iostream>

using std::cout;
using std::endl;

class Base
{
    public:
        void show()
        {
            cout << "Base class" << endl;
        }
};

class Derived: public Base
{
    public:
        void show()
        {
            cout << "Derived Class" << endl;
        }
};

int main()
{
    Base *b;       //Base class pointer
    Derived d;     //Derived class object
    b = &d;

    // The standard use of overriding
    d.show();      // ??

    // b is a pointer of parent type pointing to a child object
    // Which show() is called?
    b->show();     //Early Binding Occurs ??

    return 0;
}
