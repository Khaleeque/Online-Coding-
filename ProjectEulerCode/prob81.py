#Reading input file
matrix = []
with open("prob81_input.txt", 'rt') as f:
    for line in f:        
        matrix.append(map(int, line.strip().split(',')))

#print matrix[0][0]

#print matrix[1][0]        

m_len = len(matrix)
#print m_len


for k in range(m_len-2,-1,-1):
    matrix[m_len-1][k] += matrix[m_len-1][k+1]

for l in range(m_len-2,-1,-1):
    matrix[l][m_len-1] += matrix[l+1][m_len-1]    

#print matrix

for i in range(m_len-2,-1,-1):
    for j in range(m_len-2,-1,-1):

        
            
        if matrix[i+1][j] < matrix[i][j+1]:
            matrix[i][j] += matrix[i+1][j]
        else:
            matrix[i][j] += matrix[i][j+1]

            
print matrix[0][0]

