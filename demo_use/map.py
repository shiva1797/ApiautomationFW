# l=[1,2,3,4,5]
#
# def mul(a):
#     return a*a
#
# res=list(map(mul,l))
#
# print(res)

# A simple decorator function
def decorator(func):
    def wrapper(*args):
        print("Before calling the function.")
        res=func(*args)
        return res*res
        print("After calling the function.")
    return wrapper

# Applying the decorator to a function
@decorator

def greet():
    return 10+10

print(greet())


