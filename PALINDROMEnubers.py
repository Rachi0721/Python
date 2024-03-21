n = int(input())
m = int(input())
r = 0
for i in range(n,m,1):
    while i > 0:
        rem = n%10
        r = r*10+rem
        i = i//10
print(r,end = ' ')
 
