n = int(input( ))
data = list(map(int,input( ).split( )))
dic = { }
data.sort( )
for i in data:
    f = i%10
    if f not in dic:
        dic[f]=1
    else:
        dic[f]+=1
