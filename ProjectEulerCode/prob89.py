#Reading input file



romans = open("prob89_input.txt", 'rt').read().splitlines()

A = ''
B = ''

for s in romans:
    A += s
    
    s=s.replace("DCCCC", "CM")
    s=s.replace("LXXXX", "XC")
    s=s.replace("VIIII" , "IX")
    s=s.replace("IIII" , "IV")
    s=s.replace("XXXX", "XL")
    s=s.replace("CCCC" , "CD")
    B += s   
  

print len(A) - len(B)

