a=open('hollow_pyramid.dat','w')



for row in range(1,11):
    for col in range(1,20):
        if row==10 or row+col==11 or col-row==9:
            a.write('*'+'')
        else:
            a.write(' ')
    a.write('\n')


a.close()
