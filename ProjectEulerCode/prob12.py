
import math

#prints wrong output for 1 & squared numbers

def num_of_divisors(n):
    count = 2
    k = int(math.sqrt(n)) + 1
    for i in range(2,k):
        if n%i == 0 :
            count += 2
    return count


max = 0
for n in range(1,100000):
    triang_num = n*(n+1)*(0.5)

    nod = num_of_divisors(triang_num) 
    if  nod > max :
        max = nod
        
    if nod > 500 :        
        print nod
        print triang_num
        break
print max    
print 'end'
