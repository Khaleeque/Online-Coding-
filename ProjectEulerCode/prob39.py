llist = []

count = 0
max_count = 0
with open("prob39_input.txt",'rt') as f:
    old_ssum = 0    
    for line in f:
        a =  line.strip().split('\t')
        
        ssum = sum((int(a[0]),int(a[1]),int(a[2])))        
        if ssum <= 1000 :
            llist.append(ssum)



i_prev = 0
count = 1
max_count = 0
max_count_num = 0

sl = sorted(llist)

for i in sl:
    if i == i_prev:
        count +=  1
    else :                
        if count > max_count:
            max_count = count
            max_count_num = i_prev
            count = 1
        i_prev = i
print "==="           
print max_count,
print "times",
print max_count_num
print 'end'

print sl


# second part not working
        
