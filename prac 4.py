a = int(input( ))
b = int(input())
c = 1
i = 2
while True:
    if a%i == 0 and b%i == 0:
           a = a//i
           b = b//i
           c = c*i
    elif a <= c or b<=c:
            
            c = c*a*b
            break
    else:
            i += 1
print(c)
