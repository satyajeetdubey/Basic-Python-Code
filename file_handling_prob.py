a=open('table.dat','w')

for i in range(1,11):
    for k in range(1,11):
        
        a.write(str(i*k)+'\t')
    
    a.write('\n')

a.close()
        
