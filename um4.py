from re import L


def add(a, b):
    return a + b 


print(add(5,10))

def f(a,L = []):
    L.append(a)
    return L

print(f(2))

def findSquares(L=[],Q=[]):
    for i in range(1, 11):
        L.append(i**2)
        Q.append(i**3)
    return L,Q

sq,cb = findSquares()

print(sq)
print(cb)





