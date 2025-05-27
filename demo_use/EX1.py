# name = input("Enter your name: ")
# print(f"Hello, {name} ! Welcome!")
#
#
# print(type(name))
#
#
# a = 15
# b = 4
#
# # Division
# print("Division:", a / b)
#
# # Floor Division
# print("Floor Division:", a // b)
from math import floor

# a=3.1
#
# print(ceil(a))

# age = int(input("enter age"))
#
# if age >= 18:
#     print("Eligible to vote.")
# elif age< 18:
#     print("not adult")
# else:
#     print("not eligible")


#
# number = 1
#
# match number:
#     case 1:
#         print("One")
#     case 2 | 3:
#         print("Two or Three")
#     case _:
#         print("Other number")
#
#
# while (cnt < 3
#     print("Hello Geek")
#
# for i in range(2,10,2):
#     print(i,end=" ")
#
# for i in range(5):
# #     for j in range(5):
# #         print(j, end=' ')
# #     print()
#
# def fun():
#     name = "Alice"
#     age = 30
#     return name, age
#
# name, age = fun()
# # print(name)
# # print(age)   # Output: 30
#
#
# def mul_arg(*ar):
#     print(ar)
#
#
# mul_arg(2,3,4,5,"hdhd","dhdh")

#
# def fun(**kw):
#     for k in kw.keys():
#         print(k)
# #
# # fun(a=1, b=2, c=3)
#
# s1 = 'GeeksforGeeks'
#
# s2 = lambda func: func.upper()
# print(s2(s1))

# a=10
# b=20
#
# res = lambda a,b: a+b
#
# print(res(a,b))

n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"

print(n(-4))

#
# s= "shiva kumar "
#
# print(s[1:4])
# print(s.index("v"))
# print(s.index("v"))

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
#
# for row in matrix:
#     for val in row:
#         print(val,end=" ")
#         print()

#
# d = { "name": "Alice", 1: "Python", (1, 2): [1,2,4] }
#
# print(d.get(1))
#
# d.update({1:"cpp"})
# print(d.get(1))
# d = {1: 'Geeks', 2: 'For', 'age':22}
#
# # Iterate over keys
# for key in d.keys():
#     print(key)
#
# for val in d.values():
#     print(val)

#
# a = [2,3,4,5]
#
# res= [ i *3 for i in a ]
# print(res)

#
# a = [1, 2, 3, 4, 5]
#
# even = [ i for i in a if i%2==0]
#
# print(even)
#
# n = 10
# try:
#     res = n / "s"# This will raise a ZeroDivisionError
#
# except ValueError:
#     print("Can't be divided by str!")

import pytest

@pytest.fixture(scope="module")  # Runs once per module
def db_connection():
    print("\nSetting up DB Connection")
    yield "DB Connected"
    print("\nClosing DB Connection")  # Teardown

def test_1(db_connection):
    assert db_connection == "DB Connected"

def test_2(db_connection):
    assert db_connection == "DB Connected"






