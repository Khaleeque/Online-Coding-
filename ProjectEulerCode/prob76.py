ways = [0]*101
ways[0] = 1


for i in xrange(1,100):
    for j in xrange(i,101):        
        ways[j] += ways[j-i]

print ways[100]        
