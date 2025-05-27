# name= input("enter name: ")
# print(f"my name is {name}")
from statistics import multimode

# name1,place=input("enter name and place: ").split()
# print(f"name:{name1},place:{place}")
l=[12,  1, 10, 39, 1]
def sec_max(l):
    fir=sec=float("-inf")

    for n in l:
        if n>fir:
            fir,sec=n,fir

        elif n>sec<fir:
            sec=n
    return sec


print(sec_max(l))
#
# def decorator(func):
#     def wrapper (*args):
#         print("before mult")
#         res=func(*args)
#         return res*res
#     return wrapper
#
#
# @decorator
# def add(a,b):
#     return a+b
#
# res1=add(10,10)
# print(res1)
#
#
# l1=["a","b","c","d"]
# l2=[1,2,3,4]
# l3=dict(zip(l1,l2))
# print(l3)
#
# d2={}
# for k,v in zip(l1,l2):
#     d2[k]=v
# print(d2)
#
# d3={k1:v1 for k1,v1 in zip(l1,l2)}
# print(d3)
#
#
# a=222222
# assert type(a)==str


for i in range(11):
    if i==3:
        continue
print(i)


age =19

res= "adult"if age>18 else "child"
print(res)



cnt=0

while cnt<=5:
    print(cnt)
    cnt+=1

d = dict({'x': 123, 'y': 354})
for i in d:
    print(f"{d[i]}")



for i in range(7):
    for j in range(i):
        print(i,end=" ")
    print()


def keywors_args(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}:{v}")


keywors_args(a="apple",b="bat",c="cat")

