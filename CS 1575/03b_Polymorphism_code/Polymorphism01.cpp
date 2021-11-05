/**
  Overriding functions
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
    Base b;       //Base class object
    Derived d;     //Derived class object

    b.show();     //Early Binding Ocuurs
    d.show();      // ??

    // What happens to the base show function in the derived class? Is it still there?
    d.Base::show(); // ??

    return 0;
}


/**
  Connecting the function call to the function body is called Binding. When it is done before the program is run, its called Early Binding, Static Binding, Compile-time Binding, or method overloading
 **/
