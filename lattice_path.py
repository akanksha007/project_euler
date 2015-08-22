"""
How many such routes are there through a 20x20 grid?
"""
size_of_grid=20
#to find the precomputed value.
def memoize(f):
    memo={}
    def helper(x,y):
        if (x,y) not in memo:
            memo[(x,y)]=f(x,y)
            
        return memo[(x,y)]
    return helper

    
@memoize
#to find the different path possible for a given coordinate
def position(x,y):
    
    count=0
    global size_of_grid
    if(x==size_of_grid or y==size_of_grid):
        
         count=count+1
         return count
    else:
        return position(x,y+1)+position(x+1,y)
    
total_path=position(0,0)
print "Total no of routes possible in 20x20 grid is \n",total_path

