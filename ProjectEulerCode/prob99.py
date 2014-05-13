import math

max = 1
count = 0
print_count  = 1
#Reading File Input
with open("prob99_input.txt",'rt') as f:
    for line in f:
        count += 1
        a,b = map(int,line.split(','))
        c = b*(math.log(a)) 
        if  c > max:
            max = c
            maxi = a,b
            print_count = count
print print_count

        
