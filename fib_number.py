"""
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""
a = 1
b = 0
index = 1
while len(str(a)) != 1000:
    a, b = a+b, a
    index = index + 1
print "The index of the first term in the Fibonacci sequence to contain 1000 digits: \n",index
