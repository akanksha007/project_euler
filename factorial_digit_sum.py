"""
Find the sum of the digits in the number 100!
"""
import math
output_num=0
input_num=str(math.factorial(100))
for i in input_num:
    output_num=output_num+int(i)
print output_num
