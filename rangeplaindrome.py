n = int(input( ))
m = int(input( ))
for num in range(n,m+1):
    temp = num
    res= 0
    k = len(str(num))-1
    while(temp>0):
        rem = temp%10
        sum+=rem*pow(10,k)
        temp = temp//10
        k-=1
        if (num == res):
            print("%d"%temp,end = " ")
            
        
