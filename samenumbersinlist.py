n = int(input( ))
d = list(map(int,input( ).split( )))
dic = { }
n = int(input( ))
m = list(map(int,input( ).split( )))
for i in d:
    dic[i]=1
for i in m:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
c = 0
for i,j in dic.items( ):
    if j == 2:
        c+=1
        print(i,end= " ")
        vi = i
print( )
r = 0
for i,j in dic.items( ):
    if j == 1:
        r+=1
        print(i,end= " ")
        vb = i
print( )
print(c)
print(r)
g = min(vi)
h = min(vb)
print(g)
print(h)

        

        
        

