#Reading input file
matrix = []

sum = 0

with open("prob13_input.txt", 'rt') as f:
    for line in f:        
        #matrix.append(int(line))
        sum += int(line)

print sum    


