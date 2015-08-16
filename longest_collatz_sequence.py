import time
max_value=0
dicts={}
def chain_length(n):
    global dicts
    temp=n
    cached_max_value=0
    c=0
    while(temp!=1):
        
        if(temp%2==0):
            if temp in dicts:
                cached_max_value=dicts[temp]
                
                c=c+cached_max_value
                cached_max_value=0
                return c
            else:
                c=c+1
                
                temp=temp/2
                
        else:
            if temp in dicts:
                cached_max_value=dicts[temp]
                c=c+cached_max_value
                cached_max_value=0
                return c
            else:
                temp=3*temp+1
                c=c+1
                
    return c

for i in xrange(999999,1,-1):
    n=chain_length(i)
    dicts[i]=n
    #print n
    if(n>max_value):
        max_value=n 
#print dicts       
print max_value

