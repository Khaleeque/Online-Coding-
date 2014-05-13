import math
import itertools

def d(n):
    sum = 1
    for i in range(2,int(math.sqrt(n))+1) :
        if n%i == 0:
            sum += i + n/i
    if n == (int((math.sqrt(n)))**2) :
         sum = sum - math.sqrt(n)
    return int(sum)


abnums = []

for j in range(1,28124):
    if d(j) > j :
        abnums.append(j)
print 'len of abnums',
print len(abnums)

lisst = []

for i in abnums:
    for j in abnums:
        temp = i + j
        if temp <= 28123 :
            lisst.append(temp)

print 'len of sums of abnums',        
print len(lisst)
ss = set(lisst)
print len(ss)

kk = sum(range(1,28124))

print kk - sum(ss )


"""

        
l_s = sorted(list(s))
ll_s = len(l_s)
ss = set()


for i in range(0,ll_s):
    for j in  range(i,ll_s):
        ads = l_s[i] +l_s[j]

        if ads > 8123:
            break
        else:
            ss = ss.union([ads])
                        

kk = range(1,28124)



print sum(list(set(kk) - ss))
"""

