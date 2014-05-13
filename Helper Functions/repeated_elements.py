a='011'
temp=a[0]
cnt=0
b=[]
for i in range(len(a)):
    if(a[i] == temp):
        cnt+=1
    else:
        b.append((a[i-1],cnt))
        cnt=1
        temp=a[i]

b.append((a[-1],cnt))
print b
