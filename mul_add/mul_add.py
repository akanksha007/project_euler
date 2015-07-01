#sum of all the multiples 3 or 5 below 1000
mul_three=[];           #to store all multiples of 3
mul_five=[];            #to store all multiples of 5
total=0
for i in range (1,1000):
    a=i % 3;
    b=i % 5;
    if(a==0):
        mul_three.append(i)
    if(b==0):
        mul_five.append(i)

mul_three=mul_three + mul_five  #to combine multiples of 3 and 5
mul_three=list(set(mul_three))  #to eliminate duplicates
a=len(mul_three)
for i in range(0,a):
    total=mul_three[i]+total

print "The sum of all multiples of 3 or 5 is",total


