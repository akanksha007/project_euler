"""
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""
fib=[]
fib.append(2)
fib.append(8)
for i  in range(0,50):
    temp=fib[i+1]*4+fib[i]
    if(temp>=4000000):
        break
    else:
        fib.append(temp)
n=len(fib)

total=0
for j in range(0,n):
    total=total+fib[j]
print"the sum of even terms of fibonacci series where the value of last term in the series is less than 4000000 \n",total
