def pal(n):
    rev = 0
    while n:
        d = n%10
        n = n//10
        rev = rev*10+d
    return rev
n = int(input( ))
if n == pal(n):
    print(n)
else:
    i=1
    while True:
        if n+i == pal(n+i):
            V = (n+i)
            break
        i+=1
    while True:
        if n-i == pal(n-i):
            R = (n-1)
            break
        i+=1
    if abs(n-V)>=abs(n-R):
        print(R)
    else:
        print(V)
