import math

def n_c_r(n,r):
    return (math.factorial(n)/(math.factorial(n-r)*math.factorial(r)))

count = 0

for n in range(1,101):
    for r in range(1,n):
        if n_c_r(n,r)/1000000 > 0:
            count += 1

print count            
    
