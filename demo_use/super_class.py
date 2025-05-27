class A:
    def __init__(self,c):
        self.var_a = "I am from A"

class B:
    def __init__(self,a):
        self.var_b = "I am from B"

class C(A, B):
    def __init__(self,a,f):
        # Call parent constructors (super() only calls the first in MRO)
        A.__init__(self,a)
        B.__init__(self,f)
        self.var_c = "I am from Child"

# Create object of child
obj = C(10,30)
obj.var_a = "im also from a"
print(obj.var_a)




# a=10
# b=222
#
# res= lambda c=a:a+2+b
# print(res(b))
#
#
# def even(a):
#     return a*a
#
# a=[1,2,4,5,6,7,8,8]
#
# res=list(map(even,a))
#
# print(res)
