def reverse(n):
    rev=0
    while n:
        d = n%10
        n=n//10
        rev = rev*10+d
    return rev
n = int(input( ))
print(n==int(str(n)[::-1]))
