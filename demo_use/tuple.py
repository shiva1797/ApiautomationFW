# li = [lambda arg=x: arg * 1 for x in range(1, 5)]
# for i in li:
#     print(i())


check = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check(267))

s = ['1', '2', '3', '4']
res = map(int, s)
print(res)


def decorator1(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")

    return wrapper


# Applying the decorator to a function
@decorator1
def greet():
    print("Hello, World!")


greet()

class Public:
    def __init__(self,name):
        self.name = name  # Public attribute

    def display_name(self):
        print(self.name)  # Public method

obj = Public("shivakkkk")
obj.display_name()  # Accessible
print(obj.name)  # Accessible

n = 10
try:
    res = n / "s" # This will raise a ZeroDivisionError

except ZeroDivisionError:
    print("SORRY CANT DIVIDE")

