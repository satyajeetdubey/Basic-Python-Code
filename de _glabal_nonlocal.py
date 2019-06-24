def update():
    def first():
        a=12
    def second():
        nonlocal a
        a=23
    def third():
        global a
        a=100


    a=20
    first()
    
    print(a)
    second()
    
    print(a)
    third ()
    
    print(a)


a=11
update()
print(a)


