n_o = 3
d_o = 2

count = 0
for i in xrange(999):
    n = n_o + 2*d_o
    d = n_o + d_o
    d_o = d
    n_o = n
    if len(str(n)) > len(str(d)):
        count += 1
print count
