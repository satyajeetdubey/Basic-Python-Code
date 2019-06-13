s=input("Enter a string ")
count1_lower=0
count2_upper=0
count3_space=0
new_str=''
for a in s:
    if (a.isupper())==True:
        count2_upper+=1
        new_str+=a.lower( )
    elif (a.islower())==True:
        
        count1_lower+=1
        new_str+=a.upper( )
    elif (a.isspace())==True:
        count3_space+=1
        new_str+=a
print("no. of upper char.",count2_upper)
print("no. of lower case.",count1_lower)
    
  
print("No.of space",count3_space)
print("new str")
print(new_str)
#write a program of str in which no. of upper ,lower case and space and also convert the upper in lower and vice versa
