s=input("Enter the string ")
count_upper=0
count_lower=0
count_num=0
count_special=0
for s in s:
    if s>="A" and s<="Z":
    
        count_upper+=1
    elif s>="a" and s<="z":
        count_lower+=1
    elif s>="0" and s<="9":
        count_num=count_num+1
    else:
        count_special+=1
print("upper",count_upper)
print("lower",count_lower)
print("num",count_num)
print("special char",count_special)

    
    
