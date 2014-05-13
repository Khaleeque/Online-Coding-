import math
tot_sum = 0
for i in range(10,10000000):
    sum = 0
    for c in str(i) :
        sum = sum + math.factorial(int(c))
    if sum == i:
        tot_sum = tot_sum + i
        print i
        
print 'end'
print tot_sum
