import math
ls1 = []
found = False

for n in range(1000,10000):
    for m in range(1,n):
        k = n*(3*n - 1) + m*(3*m - 1)
        z = n*(3*n - 1) - m*(3*m - 1)

        temp1 = math.sqrt(1 + 12*k)        
        if temp1 == int(temp1) :            
            temp2 = (1 + temp1)/6
            if temp2 == int (temp2):
                temp3 = math.sqrt(1 + 12*z)        
                if temp3 == int(temp3) :
                    temp4 = (1 + temp3)/6
                    if temp4 == int (temp4):
                        ls1.append((n,m))
                        print z/2
                        found = True
        if found == True:
            break

print ls1        
