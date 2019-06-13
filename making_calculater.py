def add(x,y):#define function for adding
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    return x/y
print("Select operation.")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.division")
choice=input("Enter a choice (1,2,3,4) :")#choice for users
num1=eval(input("Enter a first no.:"))
num2=eval(input("Enter a second no.:"))
if choice=="1":#"1" because it also in str
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=="2":
    print(num1,"-",num2,"=",subtract(num1,num2))
elif choice=="3":
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice=="4":
    print(num1,"/",num2,"=",division(num1,num2))
else:
    print("wrong choice")
