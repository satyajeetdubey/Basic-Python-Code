



row1=int(input("Enter a row :"))
coloum1=int(input("Enter a coloum :"))
A=[]
for i in range(row1):
    tem=[]
    for j in range(coloum1):
        num=eval(input("Enter a number :"))
        tem.append(num)
        
    A.append(tem)
print(A)





