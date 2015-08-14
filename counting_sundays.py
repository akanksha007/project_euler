"""
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
import time
day={'Monday':0,'Tuesday':1,'Wednesday':2,'Thursday':3,'Friday':4,'Saturday':5,'Sunday':6}
present_year_day=1
count=0
def count_sunday(year,day):
    global count
    
    for i in range(1,13):
        if(day==6):
            count=count+1
        if(i==4 or i==6 or i==11 or i==9):  # month with 30 days
            day=(day+2)%7
            
        elif(i==2):                     #feb:checking for leap year
            if(year%4!=0):
                day=day
            else:
                day=(day+1)%7
                 
        else:                               #month with 31 days
            day=(day+3)%7  
   
    return(count,day)
    
for i in range(1901,2001):
    count,present_year_day=count_sunday(i,present_year_day)
    #print count,i
    #time.sleep(1)

print "\nSundays that fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000) :\n",count

                
