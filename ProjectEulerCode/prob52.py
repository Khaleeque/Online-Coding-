

x = 1
found = 0

while(found == 0):
    x = x + 1

    a = x
    a_a = []
    while(a!=0):
        a_a.append(a%10)
        a /= 10
    a_a.sort()

    a = 2*x
    b_a = []
    while(a!=0):
        b_a.append(a%10)
        a /= 10
    b_a.sort()  

    a = 3*x
    c_a = []
    while(a!=0):
        c_a.append(a%10)
        a /= 10
    c_a.sort()  

    a = 4*x
    d_a = []
    while(a!=0):
        d_a.append(a%10)
        a /= 10
    d_a.sort()  

    a = 5*x
    e_a = []
    while(a!=0):
        e_a.append(a%10)
        a /= 10
    e_a.sort() 
    
    a = 6*x
    f_a = []
    while(a!=0):
        f_a.append(a%10)
        a /= 10
    f_a.sort()     

   
    if a_a == b_a == c_a == d_a == e_a == f_a :
        print x
        found = 1
  










