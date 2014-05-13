ways = 0


for i in range(0,1):
    for j in range(0,3):
        for l in range(0,5):
            for m in range(0,11):
                for n in range(0,21):
                    for o in range(0,41):
                        for p in range(0,(101- o*5/2)):
                            for k in range(0,201):
                               
                                sum =200*i +100*j +50*l+20*m+10*n+5*o+2*p +k*1
                                if sum == 200:
                                    ways +=1
                                if sum > 200:
                                    break
                                

print ways                            


#>>> 
#73681
# plus 1 for i = 1
#73682

