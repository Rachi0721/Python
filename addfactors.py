def fact(n):
    if (n==1):
        return 1
    return n*fact(n-1)
n= int(input( ))
p=n
ans  = 0
while(n!=0):
    d = n%10
    n = n//10
    res = fact(d)
    ans = ans+res
if (p == ans):
    print("the number",p,"is a strong number")
else:
    print("the number",p,"is not a strong number")
    
    
