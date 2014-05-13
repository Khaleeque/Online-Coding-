import math
def d(n):
    sum = 1
    for i in range(2,int(math.sqrt(n)) + 1) :
        if n%i == 0:
            sum += i + n/i
    return sum


s = set()

for j in range(1,10000):
    if d(d(j)) == j:
        if d(j) != j:
            s = s.union([j])

print s        
print sum(s)    
