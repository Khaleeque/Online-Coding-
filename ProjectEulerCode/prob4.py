
found = 0
    
list = []
for i in range(999,99,-1):
    for j in range(999,99,-1):
        prod = i*j
        s_prod  = str(prod)
        rs_prod = s_prod[::-1]
        if(rs_prod == s_prod):
            list.append(s_prod)
          
list.sort()

        
    

print max(x * y
    for x in xrange(100,1000)
        for y in xrange(100,1000)
            if str(x*y) == str(x*y)[::-1])
