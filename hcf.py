a = int(input( ))
b = int(input( ))
if b>a:
      a, b = b , a
for i in range(b,0,-1):
       if b%1 == 0 and a%1 == 0:
              print(i,"is a HCF")
              break
