import math






target = 2000000
ans = 0
ansarea =0

for x in range(2000):
    for y in range(2000):

        rects = (x*(x+1)*y*(y+1))/4
        

        if math.fabs(rects-target) < math.fabs(ans- target):
            ans = rects            
            ansarea = x*y

print ansarea            

        
        
