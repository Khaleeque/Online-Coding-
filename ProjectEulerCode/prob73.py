counter = 0

for q in xrange(12000,1,-1):
    p = ((q - 1))/2

    count = 0
    while True:
        if 3*p > q :
            count += 1
        else:
            break
        p -= 1
    counter += count
    
print counter
