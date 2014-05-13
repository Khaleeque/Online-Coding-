def ispandigital(x):
    s = set()
    for c in str(x):
        s = s.union([int(c)])    
    if s == set([1,2,3,4,5,6,7,8,9]) :
        return True
    else:
        return False
    
        



max_concat_prod = 918273645




for x in range(90,100):
    temp = ''
    stop = False
    i = 0
    while(stop != True):
        i +=1
        temp = temp + str(x*i)        
        if len(temp) >9:
            stop = True
        elif len(temp) == 9:
            if ispandigital(int(temp)):
                if int(temp) > max_concat_prod :
                    max_concat_prod = int(temp)
                print int(temp)
        
    
for x in range(900,1000):
    temp = ''
    stop = False
    i = 0
    while(stop != True):
        i +=1
        temp = temp + str(x*i)
        if len(temp) >9:
            stop = True
        elif len(temp) == 9:
            if ispandigital(int(temp)):
                if int(temp) > max_concat_prod :
                    max_concat_prod = int(temp)
                print int(temp)

for x in range(9000,10000):
    temp = ''
    stop = False
    i = 0
    while(stop != True):
        i +=1
        temp = temp + str(x*i)
        if len(temp) >9:
            stop = True
        elif len(temp) == 9:
            if ispandigital(int(temp)):
                if int(temp) > max_concat_prod :
                    max_concat_prod = int(temp)
                print int(temp)

            


                
print "the answer is  : " + str(max_concat_prod)
