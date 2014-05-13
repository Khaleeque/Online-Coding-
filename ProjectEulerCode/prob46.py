from prime_check import isprime

for num in range(2,10000):
    if num & 1:
        if not isprime(num):
            for i in range(1,num):
                if num - 2*i*i < 0:
                    print num
                    break
                
                if isprime(num - 2*i*i):                    
                    break
print 'end'
            
                
        
        

       
