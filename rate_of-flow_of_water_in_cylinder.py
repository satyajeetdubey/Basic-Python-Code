a=eval(input("Enter a time :"))
r=5
h=15
#vol1 =(22/7)*(r**2)*h#vol1=785.56 cylinder capacity
vol1=1177.5
vol=a*15#rate=vol/time
if vol1>vol:
    print("under flow")
elif vol1<vol:
    print("over flow")
else:
    print("filled")
#a cylinder have radius 5 and height 15 and a pump filled water at rate 15vol/min the programming the condition for filled overflow and under flow
