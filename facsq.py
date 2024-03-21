''''from math import sqrt
def factcount(n):
    if n==1:
        return 1
    s = int(sqrt(n))
    fc = 2
    for i in range(2,s+1):
        if n%i == 0:
            fc+=2
    if s*s==n:
        fc-=1
    return fc
    
n = int(input( ))
print(factcount(n))'''

from math import sqrt
def factcount(n):
    if n==1:
        return 1
    s = int(sqrt(n))
    fc = 2
    for i in range(2,s+1):
        if n%i == 0:
            fc+=2
    if s*s==n:
        fc-=1
    return fc
    
n = int(input( ))
print(factcount(n)
