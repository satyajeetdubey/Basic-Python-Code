#Write a Python program to map two lists into a dictionary.
list1=['name','age','interest']

list2=['satyajeet',19,'programming']



#dict1=dict(zip(list1,list2))   ----second but prefer first

dict1={}

for i in range(len(list1)):
    

    
    
    dict1[list1[i]]=list2[i]
    


   


print(dict1)
