def isnotlychrel(n):
    count = 1
    while count != 50 :        
        snns = n + int(str(n)[::-1])
        if snns == int(str(snns)[::-1]):
            return True
        n = snns
        count +=1
    return False


        
l_count = 0
for i in range(1,10000):
    if not isnotlychrel(i) :
        l_count +=1
print l_count
               
               
               
               

print islychrel(47)

print islychrel(10677)

        
  
