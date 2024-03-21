n =  int(input())
r = 0
a = n
while n > 0:
    rem = n%10
    r = r*10+rem
    n = n//10
print(r)
if a == r:
    print("palindrome")
else:
    print("not a palindrome")
    
