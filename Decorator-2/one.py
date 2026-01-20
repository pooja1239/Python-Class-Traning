def smart_div(func):

    def inner(a,b):
        if b==0:
            print('cannot devide by zero')
        else:
            return  func(a,b)
    return inner

@smart_div
def Calc(a,b):
    print(a/b)  

Calc(10,5)
Calc(10,0)                  