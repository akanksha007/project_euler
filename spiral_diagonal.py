"""
Starting with the number 1 and moving to the right in diagonal_list clockwise direction diagonal_list 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
It can be verified that the sum of the numbers on the diagonals is 101.
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""
diagonal_list = []
x,y,z = 0,0,3

# loop to generate the right diagonal
for i in xrange(1,1002):
    if(i % 2 == 0):
        diagonal_list.append(i**2 + 1)
    else:
        diagonal_list.append(i ** 2)
        
# loop to generate the left diagonal upper part        
for i in range(3,1002,2):
    x = x + 2
    diagonal_list.append(i * i - x)

diagonal_list.append(3)  
 
# loop to generate the left diagonal lower part
for i in range(5,1002,2):
    y = y + 2
    diagonal_list.append(z * i - y)
    z = i
    
print" The sum of the numbers on the diagonals in 1001 by 1001 spiral formed is:\n" ,sum(diagonal_list)   
