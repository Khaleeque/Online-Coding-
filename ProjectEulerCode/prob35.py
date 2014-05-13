
# prime numbers are only divisible by unity and themselves
# (1 is not considered a prime number by convention)
def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True
# test ...


no_circ_primes = 0
for x in range(1,1000000):
    if isprime(x):
        stop = False
        temp = x
        while (stop != True):            
            temp = (temp/10)+ (10**(len(str(temp)) -1))*(temp%10)
            if isprime(temp) == False :
                stop = True
            if temp == x:
                stop = True
                no_circ_primes += 1

print no_circ_primes          
            
             
                 
                    
            
                                    
                                    
                                    
                                    
    



