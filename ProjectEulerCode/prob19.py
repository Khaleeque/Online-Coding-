import calendar

count = 0

for yr in range(1901,2001):
    for mnth in range(1,13):
        if calendar.weekday(yr,mnth,1) == 6:
            count += 1
            
print count




def isleap(yr):
    if yr%100 == 0:
        if yr%400 !=0 :
            return False
    if yr%4 == 0:
        return True
    return False

def daysmnth(mnth,yr) :
    if mnth in [1,3,5,7,8,10,12]:
        return 31
    if mnth in [4,6,9,11]:
        return 30
    else:
        if isleap(yr):
            return 29
        else:
            return 28

count = 0
day = 1 #First day of January 1901 is Tue

for yr in range(1901,2001):    
    for mnth in range(1,13):
        if day == 6:
            count += 1        
        day = (day + daysmnth(mnth,yr))%7
    
        

print count        

