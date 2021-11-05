
# Test whether the relation is an equvilence relation.


Dom = range(5)

Rel1 = [ ]
Rel1.append((0,0))
Rel1.append((0,4))
Rel1.append((0,5))
Rel1.append((1,1))
Rel1.append((1,3))
Rel1.append((2,2))
Rel1.append((3,1))
Rel1.append((3,3))
Rel1.append((4,0))
Rel1.append((5,0))
Rel1.append((4,4))
Rel1.append((5,5))


print("Rel1 =",Rel1)
print(60*"*")

def Reflexive(D,R):
    for x in D:
        if (x,x) not in R:
            return False
    return True

def Symmetric(R):
    for (a,b) in R:
        if (b,a) not in R:
            return False
    return True


def Transitive(R):
    for (a,b) in R:
        for (c,d) in R:
            if (b == c) and ((a,d) not in R):
                print(a,b,c,d)
                return False
    return True


print("Reflexive(Dom,Rel1) =",Reflexive(Dom,Rel1))

print(60*"*")
print("Symmetric(Rel1) =",Symmetric(Rel1))

print(60*"*")
print("Transitive(Rel1) =",Transitive(Rel1))








