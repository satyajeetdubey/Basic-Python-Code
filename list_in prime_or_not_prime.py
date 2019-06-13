a=list(range(1,101))
list1=[]
list2=[]
for i in a:
    for j in range(2,i):
        if i%j==0:
            
            list2.append(i)
            break
        
    
        else:
            if not i<=1:
                list1.append(i)






print("prime list \n",list1)
print("Not prime list \n",list2)
