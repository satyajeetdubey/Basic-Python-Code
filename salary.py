sum=0
with open("intro.txt","r") as fp:
    for i in fp.readlines():
        sum=sum+int(i)
    print(sum)