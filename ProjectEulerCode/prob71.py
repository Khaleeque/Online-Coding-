
r = 0
s = 1

for q in xrange(1000000,1,-1):
    p = ((3*q - 1))/7

 
    if r*q < p*s:
        r = p
        s = q
print r,s   
    
