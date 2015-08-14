"""
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
def gcd(a,b):
    while b:      
        a, b = b, a % b
    return a
    
flag=False
lcm=reduce(lambda lcm,y:lcm*y/gcd(lcm,y),range(2,21)) #to find the lcm of 1to 20
#to  check if lcm is evenly divisible 
while(flag!=True):
    c=0
    for i in range (2,21):
        if (lcm/i)%2==0:
            c=c+1
        else:
            lcm=lcm+lcm
            break
    if c==19:
        flag=True
print lcm    
