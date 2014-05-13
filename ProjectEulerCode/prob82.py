#Reading input file
matrix = []
with open("prob82_input.txt", 'rt') as f:
    for line in f:        
        matrix.append(map(int, line.strip().split(',')))
  

m_len = len(matrix)

sol =[0]*m_len



for j in range(m_len-2,-1,-1):    
    

    #Traversing down
    sol[0] = matrix[0][j] + matrix[0][j+1]
    for i in range(1,m_len):
            
        if sol[i-1] < matrix[i][j+1]:
            sol[i] = matrix[i][j] + sol[i-1]
        else:
            sol[i] = matrix[i][j] + matrix[i][j+1]
    #print '###'
    #print sol
    #print '###'
    
    #Second Sweep going up
    matrix[m_len-1][j] = sol[m_len-1]

    for i in range(m_len-2,-1,-1):
            
        if matrix[i+1][j]+ matrix[i][j] < sol[i]:
            matrix[i][j] += matrix[i+1][j]
        else:
            matrix[i][j] = sol[i]


ans = matrix[0][0]


for i in xrange(m_len):
    if ans <= matrix[i][0]:
        pass
    else:
        ans =matrix[i][0]

print 'ans =', ans            
        
"""
def eul82():
    f = numpy.array([[int(j) for j in i[:-1].split(',')] for i in open("82.txt")])
    d = numpy.array([[float('inf') for x in range(80)] for j in range(80)])
    for n in range(80): d[(n,0)] = f[(n,0)]
    q = priorityDictionary() # http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/117228
    for x,y in [(i,j) for i in xrange(80) for j in xrange(80)]: q[(x,y)] = d[(x,y)]
    for i in q:
        if i[1] == (79): break
        for j in [(i[0] + 1,i[1]), (i[0], i[1] + 1),(i[0] - 1,i[1])]:
            if 80 not in j and -1 not in j and j in q:
                v = min(d[j], d[i] + f[j])
                d[j] = v
                q[j] = v
    return min(d[:,79])
"""	