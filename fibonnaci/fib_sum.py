fib=[]
fib.append(1)
fib.append(2)
for i in range(2,4000000):
    
    a=fib[i-1]+fib[i-2]
    fib.append(a)
l=len(fib)
total=0
for i in range(0,l):
    even=fib[i]%2  
    if(even==0):
        total=fib[i]+total 
print total
