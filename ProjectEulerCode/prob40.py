irr_df = ''

for i in range(1,1000000):
    irr_df += str(i)

print len(irr_df)
print int(irr_df[99])*int(irr_df[999])*int(irr_df[9999])*int(irr_df[99999])*int(irr_df[999999])
