print("Find LCM of two number")
a=eval(input("Enter a no. :"))
b=eval(input("Enter a no. :"))
for i in range (1,a*b+1):#max. value of divisible is a*b and loop mbve count from 1 to  a*b
    if (i%a==0) and (i%b==0):#cond. for LCM
        print("LCM of two no. is",i)
        break#break the loop when find        
