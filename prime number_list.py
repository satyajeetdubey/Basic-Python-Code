a=[]
n=int(input("enter the no of eliments"))
for i in range(1,n+1):
    x=int(input("enter the eliments"))
    a.append(x)

prime_number_list=[]
composite_number_list=[]
for j in a:
    if a%j==0:
        composite_number_list.append(j)
    else:
        prime_number_list.append(j)
print(prime_number_list )
print(composite_number_list)
                          
