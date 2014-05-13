#Reading input file
matrix = []
with open("prob67_input.txt", 'rt') as f:
    for line in f:        
        matrix.append(map(int, line.strip().split(' ')))

print matrix[0][0]

print matrix[1][0]        

m_len = len(matrix)

for i in range(m_len,0,-1):
    for j in range(0,i-1):
        if matrix[i-1][j] > matrix[i-1][j+1]:
            matrix[i-2][j] += matrix[i-1][j]
        else:
            matrix[i-2][j] += matrix[i-1][j+1]

            
print matrix[0][0]
