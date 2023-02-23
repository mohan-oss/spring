def deco1(fun):
    def inner(a,b):
        if(a<b):
            a,b=b,a;
        fun(a,b)
    return inner

@deco1
def div_fun(a,b):
    print(a/b)

div_fun(2,12)