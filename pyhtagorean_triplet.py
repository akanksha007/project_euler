"""
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import sys
for a in range(100,500):
    for b in range(100,500):
        c=(500000-a*b)/1000            
        if c**2==a**2+b**2:
            print a*b*c
            sys.exit(0)
                
                
        
        
