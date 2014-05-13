a = 2
b = 3


for i in xrange(98):
    if i%3 == 0:
        m = 2*(i/3) +2
    else:
        m = 1
    c = m*b + a
    a = b
    b = c

sum = 0    
for ci in str(c):
    sum += int(ci)
print sum    
    
