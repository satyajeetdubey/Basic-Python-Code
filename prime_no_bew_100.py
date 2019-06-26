a=open('prime_number.dat','w')

for i in range(1,101):
    
    
    for j in range(2,i):
        
        if i%j==0:
            break
    
    else:
        a.write(str(i)+'\n')
                

a.close()    
