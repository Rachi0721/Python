n = int(input( ))
data = list(map(int,input( ).split( )))
dic = { }
for i  in data:
    k=i%2
    if k not in fic:
        dic[k]=1
    else:
        dic[k]+=1
for v in  dic.values( ):
    print(v,end=' ')
