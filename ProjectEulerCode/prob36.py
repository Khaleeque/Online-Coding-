getBin = lambda x: x >= 0 and str(bin(x))[2:]


sum = 0

for num in range(1,1000000):
    if str(num) == str(num)[::-1]:
        bnum = str(getBin(num))
        if bnum == bnum[::-1] :
            sum = sum + num
    

print sum

