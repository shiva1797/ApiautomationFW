def arg(*args,**kwargs):
    for i in args:
        print(i)
    for k,v in kwargs.items():
        print(k,v)

arg(53,6,6,7,77,99,00,66,88,a=99,b=22,c="ed")
