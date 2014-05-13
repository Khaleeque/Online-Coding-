f1 = 1
f2 = 1

count = 2
found = 0

while(found == 0):
    count += 1
    next = f1 + f2
    n_digit = 10**999
    if(next/n_digit != 0):
        found = 1
        print count
        print next
        break
    f1 = f2
    f2 = next
    
    
        
