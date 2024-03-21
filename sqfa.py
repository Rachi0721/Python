from math import sqrt
def factcount(n):
    if n==1:
        return 1
    s = int(sqrt(n))
    fc = 2
    for i in range(2,s+1):
        if n%i == 0:
            return [i,n//i]
    return [-1]
n = int(input( ))
print(factcount(n))
