"""
Find the largest palindrome made from the product of two 3-digit numbers.
"""

import sys,time
palindrome=[]
for i in range(999,99,-1):
    for j in range(999,99,-1):
        a=i*j
        a=str(a)
        if(a==a[::-1]):
            palindrome.append(i*j)
     
print max(palindrome)
