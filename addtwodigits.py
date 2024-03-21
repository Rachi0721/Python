n = int(input( ))
a = 0
b = 0
c = 0
ans = 0
while n>9 :
    if n>=0:
        d = n%10
        a += d
    if n>=0:
        n = n//10
        b += n
        ans  = ans +d
if ans > 9:
    r = n%10
    n = n//10
    c += r
print(c)
        
    
