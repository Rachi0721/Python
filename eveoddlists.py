n = int(input( ))
m = list(map(int,input().split( )))
c = 0
for i in m:
    if i%2 == 0:
        c+=1
print(c,len(m)-c)
