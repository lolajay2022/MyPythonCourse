def outer_function():
    #local namespace of outer
    b = 20 
    def inner_func():
        #nested local namespace of inner
        c = 30
        #b is available, but non-local here
        # cannot change b here
        #if you try it is just created a new b here

a = 10 #in global namespace


def outer_function():
    a = 20
    def inner_function():
        a = 30
        print('a =',a)

    inner_function()
    print('a =',a)
     
a = 10
outer_function()
print('a =',a)

