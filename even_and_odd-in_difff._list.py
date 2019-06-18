a=int(input("Enter a number: "))
list1=[]
list2=[]
for i in range(2,a+1):
    if i%2==0:
        list1.append(i)
    else:
        list2.append(i)
print("Even no. ",list1)
print("Odd no. ",list2)
