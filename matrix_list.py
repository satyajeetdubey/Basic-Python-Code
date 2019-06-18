r=int(input("Enter a no. of row :"))
c=int(input("Enter a no. of coloum :"))
A=[]
for i in range(r):
    tem=[]
    for k in range(c):
        num=eval(input("Enter the value :"))
        tem.append(num)
    print("child list",tem)
    
    A.append(tem)
#print("Father list",A,end="")
for i in A:
    print(i)
