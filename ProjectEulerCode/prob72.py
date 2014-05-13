limit = 1000000


phi = range(limit+1)

counter = 0

for i in xrange(2,limit+1):
    if phi[i] == i :
        for j in range(i,limit+1)[::i] :
            phi[j] = phi[j]/i*(i-1)
    counter += phi[i]

print counter    
        
