
def helper(n):    
    lsn = sorted(str(n),reverse = True)
    st = ''
    for c in lsn :
        st = st + c
    return int(st)
 
        



llist = []

for i in range(1,100000):
    icube = i**3
    if 99999999999 < icube :
        if  999999999999 > icube:
            llist.append((helper(icube),i))        
llist = sorted(llist)

def first((i,j)):
    return i


alist = map(first,llist)
cnt=0
maxnum=0
maxcnt=0
maxnum2=0
prev=0
prev2=0
for i in alist:
    if (prev==0):
        prev=i
        #prev2=i[1]
        cnt+=1
    if (prev==i):
        cnt+=1
    else:
        if cnt>maxcnt:
            maxcnt=cnt
            maxnum=prev
        cnt=1
        prev=i
    if cnt == 0 :
        break
    
    
            
print maxnum,
print maxcnt
           
print llist[alist.index(maxnum)]
print llist[alist.index(maxnum) +1]
print llist[alist.index(maxnum) +2]
print llist[alist.index(maxnum) +3]
print llist[alist.index(maxnum) +4]
print llist[alist.index(maxnum) +5]


#>>> 5027**3
#127035954683L

