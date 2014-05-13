from prime_check import isprime
list = []


for num in range(10,1000000):
    next = True
    for i in range(1,1+len(str(num))):        
        str_n = ''
        for j in range(1,i+1):
            str_n += str(num)[j-1]        
        if not isprime(int(str_n)):
            next = False
            break
    if next:
        for i in range(1,len(str(num))):
            str_n = ''
            for j in range(1,i+1):
                str_n = str(num)[len(str(num)) - j] + str_n
            if not isprime(int(str_n)):
                next = False
                break
    if next:
        list.append(num)
    if len(list) == 11 :
        print(sum(list))
        print 'found'
        break
    

               
print list               
