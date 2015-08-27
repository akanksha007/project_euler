"""
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
exponent=5
upper_bound=(exponent+1) * (9**exponent)
fifth_power=[] # list of all those no which stasify the property
for i in xrange(2,upper_bound):
    num=str(i) #to make integer iterable
    k=0 #sum of fifth power of all the digits in num
    # to calculate fifth power of all the digit in num
    for j in num:
        k=k+(int(j)**5)
    #to check if sum equls the number itself
    if(i==k):
        fifth_power.append(i)
#to find the sum of all numbers that statisfy the property
print sum(fifth_power)
        
        
                

