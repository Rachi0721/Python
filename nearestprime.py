n = int(input( ))
c = 0
for i in range(1,n+1):
    if n%i == 0:
        c+=i
if c==n:
    print(n,"prime")
else:
    print(n,"not prime")
    
