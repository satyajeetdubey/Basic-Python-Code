
def even(x):
        if x%2==0:
            return True
        else:
            return False
            
    

list1=[2,3,4,5,6,7,8]
out=list(filter(even,list1))

print(even(100))
print(out)
