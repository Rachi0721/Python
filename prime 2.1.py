n = int(input( ))
b = n//2
for i in range(2,b+1):
     if n%i == 0:
          print(n,'is not a prime number')
          break
else:
        print(n, 'is a prime number')
