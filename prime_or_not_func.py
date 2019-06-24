#a=int(input("Enter a value"))




def prime(x):
    #logic here
    for i in range(2,x):
        if x%i==0:
            return False
    #important
    else:
        return True

list1=[2,3,4,5,6,7,8,9,556,45,43]
#important

out=list(map(prime,list1))

l=list(filter(prime,list1))
#filter is give only which element which cond is true in written form but map is frint
#used for print true as wwell as false 
print(out)
print(l)
