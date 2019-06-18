r1=int(input("Enter a row M1:"))
c1=int(input("Enter a coloum M1:"))
A=[]
for i in range(r1):
    tem=[]
    for k in range(c1):
        num=eval(input("Enter a value :"))
        tem.append(num)
    A.append(tem)
r2=int(input("Enter a row M1:"))
c2=int(input("Enter a coloum M1:"))
B=[]
for i in range(r2):
    tem=[]
    for k in range(c2):
        num=eval(input("Enter a value :"))
        tem.append(num)
    B.append(tem)

if r1==r2 and c1 == c2:
    C=[]
    for i in range(r1):
        tem=[]
        for k in range(c1):
            num=0
            tem.append(num)
        C.append(tem)
    

    for i in range(r1):
        for k in range(c2):
            C[i][k]=A[i][k]+B[i][k]
for i in C:
    print(i)

