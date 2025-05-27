# for i in range(1, 5):
#     for j in range(i):
#         print(i,end="")
#     print()
# for i in range(1, 5):
#     for j in range(i):
#         print(i, end=' ')
#     print()
from statistics import multimode


# def mul_inp(*args):
#     print(args)
#     print(type(args))
#
# mul_inp(1,2,3,4,5,6,6,"jejehe")


#
# def fun(**kwargs):
#     for k, val in kwargs.items():
#         print("%s == %s" % (k, val))
#
#
# # Driver code
# fun(s1='Geeks', s2='for', s3='Geeks')

# #['k1v1','k2k21v21','k3v3']
# def dec(func):
#     def wrapper():
#         print("HI")
#         func()
#     return  wrapper
#
# d = { "name": "Alice", 1: "Python", (1, 2): [1,2,4] }
#
#
# for key,val in d.items():
#     if isinstance(key,tuple):
#
# # Access using key
# print(d["name"])
# print(d.get(1))
# # Access using get()
# print(d.get("name"))
# d[1]="pytest"
# d["place"]= "sarj"
# d.update({"area":"ban"})
# print(d)
#
#
# def hello():
#     print("hello")
#
# hello()

a = [[1, 2, 3, 4, 5],[3,4,6,7]]
res= [j for i in a for j in i]
print(res)

s="hello"
s1=""

for i in s:
    s1=i+s1
print(s1)
