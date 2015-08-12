"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
import math
n=600851475143
flag=False
# to find whether the factor of n is prime or not
def prime(n):
    if(n==2):
        return True
    if(n%2==0):
        return False
    else:
        sqr=int(math.sqrt(n))+1
        for i in range(3,sqr,2):
            if n%i==0:
                return False
    return True 
# to find if the factors of n
for i in range(1,int(math.sqrt(n))+1):
    if n%i==0:
        large_num=n/i
        flag=prime(large_num)
        if(flag==True):
            print large_num
            break
        
#to check in the smaller divisor of num if none of large number is prime           
if flag==False:
    for i in range(int(math.sqrt(n))+1,1,-1):
        if n%i==0:
            flag=prime(i)
        if(flag==True):
            print i 
            break
        
     









