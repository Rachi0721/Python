from math import sqrt
def prime(n):
    if n==1:
        return False
    s = int(sqrt(n))
    for i in range(2,s+1):
        if n%i == 0:
            return False
    return True
n = int(input( ))
if prime(n):
    print("prime")
else:
    print("not prime")
