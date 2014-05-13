from prime_check import isprime

prim_list = []
for k in range(2,1000):
    prim_list.append(k)
    
max_count = 0
for a in range(-999,999):
    for b in prim_list:        
        for i in range(0,1000):
            #print  i,
            #print isprime(i*i + a*i + b)

            if isprime(i*i + a*i + b) == False:                
                if  i > max_count :                
                     max_count = i
                     max_a = a
                     max_b = b
                break
            
print max_count
print max_a
print max_b            
print max_a*max_b
        

