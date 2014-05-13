import math

ls1 = []

for t in range(285,300000):
    temp1 = math.sqrt(1 + 12*t*t + 12*t)
    if temp1 == int(temp1) :
        temp2 = (1 + temp1)/6
        if temp2 == int (temp2):
            
            ls1.append((temp2,t))

print ls1

for n in ls1:
    temp = math.sqrt(1 + 12*n[0]*n[0] - 4*n[0])
    if temp == int(temp) :
        tempo = (1+temp)/4
        if tempo == int(tempo):          
            print n[1]
            break
    
        


#[(165.0, 285), (2296.0, 3976), (31977.0, 55385)]
#285
#k = 55385
#k*(k+1)/2
#1533776805L

