from prime_check import isprime

prim_list = []

for i in range(2,1000):
    if isprime(i):
        prim_list.append(i)

#print prim_list

for i in range(100000,140000):
    num1 = i
    num2 = i+1
    num3 = i+2
    num4 = i+3

    count = 0
    count1 = 0
    count2 = 0
    count3 = 0

    loop_count = 0

    next = False
    for j in prim_list:
        if j > num1:
            break
        
        if num1%j == 0:           
            count+= 1
            if count == 4 :
                next = True
                break

    if next:            
        next = False
        for k in prim_list:
            if k > num2:
                break
            if num2%k == 0:                
                count1+= 1
                if count1 == 4 :
                    next = True
                    break

          
    if next:        
        next = False
        for l in prim_list:
            if l > num3:
                break
                
            if num3%l == 0:                
                count2+= 1
                if count2 == 4 :
                    next = True
                    break


    if next:
        next = False
        for m in prim_list:
            if m > num4:
                break
            if num4%m == 0:              
                count3+= 1
                if count3 == 4 :
                    next = True
                    break                

    
    if next:
        print 'ans'
        print  i


print 'end'  

