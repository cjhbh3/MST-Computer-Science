/**
  For pure virtual, you can include a definition, but it can't be inline, since inline is illegal for pure virtual only.
  This is similar to pure virtual functions previously.
  Note: this is not something you would really ever do.
 **/

#include <iostream>
using std::cout;
using std::endl;

class Base
{
    public:
        virtual ~Base() = 0;     //Pure Virtual Destructor
};

Base::~Base() //Definition of Pure Virtual Destructor
{
    cout << "Base Destructor" << endl;
}

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
    Base* b = new Derived;     //Upcasting

    // Pointer of a base type pointing to a derived object
    delete b;

    return 0;
}

// back to pres
