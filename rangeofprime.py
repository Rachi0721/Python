def fun(n,m):
    for i in range(n,m+1):
        if n>=1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                print(i)
n = int(input())
m = int(input())
fun(n,m)
