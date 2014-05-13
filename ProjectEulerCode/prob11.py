#Reading input file
matrix = []
with open("prob11_input.txt", 'rt') as f:
    for line in f:        
        matrix.append(map(int, line.strip().split(' ')))



prod_max = 0

for i in range(0,20):
    for j in range(0,17):
        prod = matrix[i][j]*matrix[i][j+1]*matrix[i][j+2]*matrix[i][j+3]
        if(prod > prod_max):
            prod_max = prod
            

for j in range(0,20):
    for i in range(0,17):
        prod = matrix[i][j]*matrix[i+1][j]*matrix[i+2][j]*matrix[i+3][j]
        if(prod > prod_max):
            prod_max = prod

for i in range(0,17):
    for j in range(0,17):
        prod = matrix[i][j]*matrix[i+1][j+1]*matrix[i+2][j+2]*matrix[i+3][j+3]
        if(prod > prod_max):
            prod_max = prod


for i in range(0,17):
    for j in range(3,20):
        prod = matrix[i][j]*matrix[i+1][j-1]*matrix[i+2][j-2]*matrix[i+3][j-3]
        if(prod > prod_max):
            prod_max = prod


print prod_max
            
