def isPerm(m,n):
    digits = [0]*10

    while(m!=0):
        digits[m%10] +=1
        m /= 10

    while(n!=0):
        digits[n%10] -=1
        n /= 10

    for i in xrange(10):
        if (digits[i] !=0):
            return False
    return True

