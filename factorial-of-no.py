n=int(input("Enter a number"))



'''s=1
for  i in range(1,n+1):
    s=i*s
    



print(s)'''


def fact(x):
    if x==0:
        return 1
    #elif x == -x:
     #   print('Does not exit')
    else:
        return x*fact(x-1)



print(fact(n))
