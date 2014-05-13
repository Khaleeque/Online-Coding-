from prime_check import isprime

list_of_primes = []

num = 1000000
for i in range(1,7000):
    if isprime(i) :
        list_of_primes.append(i)


l = len(list_of_primes)
print l

for j in range ( l ,500,-1):    
    for k in range(0,l - j):
        sum  = 0
        ss =''
        for i in range(0+k,j+k+1):
            sum = sum + list_of_primes[i]                
        if isprime(sum):
            print sum
            break
            
            
            
                
    

            


