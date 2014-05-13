import itertools
    

def aptnums(sn):    
    primlist = [2,3,5,7,11,13,17]
    for i in range(1,8):
        isubsn = int(sn[i:i+3])
        if isubsn%primlist[i-1] != 0 :
            return False
    return True    
    
for i in  map(lambda x : x[0]+x[1]+x[2]+x[3]+x[4]+x[5]+x[6]+x[7]+x[8]+x[9],list(itertools.permutations('1234567890'))) :
    if aptnums(i):
        print i

print 'end'            

'''
1430952867
1460357289
1406357289
4130952867
4160357289
4106357289
end
>>> 
1430952867 + 1460357289 + 1406357289 + 4130952867 + 4160357289 + 4106357289
'''
