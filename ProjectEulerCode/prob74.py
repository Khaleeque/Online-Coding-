f = [1,1,2,6,24,120,720,5040,40320,362880]
def FSum(n):
    ret = 0
    while(n>0):
        ret += f[n%10]
        n/=10
    return ret

counter = 0
for i in xrange(1000000):
    tempList = []
    stop = False
    tempList.append(FSum(i))
    count = 0
    while (not stop) :        
        t = FSum(tempList[count])
        count +=1
        if (t in tempList):
            k = len(tempList)
            if k == 59:
                counter += 1                        
            break
        else:
            tempList.append(t)
        
print counter
