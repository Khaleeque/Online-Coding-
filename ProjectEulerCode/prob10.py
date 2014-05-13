def isprime(n):        
        
    # 2 is the only even prime number
    if n == 2: 
        return 1    
    # all other even numbers are not primes
    if not n & 1: 
        return 0
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return 0
    return 1

sum = 0

for num in range (2,2000000):
    if(isprime(num)):
        sum = sum + num

print sum        

