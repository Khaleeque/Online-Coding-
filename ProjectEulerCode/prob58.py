from prime_check import isprime
n_prims = 0
num = 1

for i in range(2,100000):
    denom = 4*i - 3    
    for a in range(1,5):
        num += 2*(i-1)
        if isprime(num):
            n_prims += 1
    if (float(n_prims)/denom) < 0.1 :
        print 2*i - 1
        break
    
    
print 'end'
