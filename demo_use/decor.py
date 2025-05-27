# # while True:
# #     name=input("enter name")
# #     if name != "":
# # #         print(name)
# # #         break
# from demo_use.while_1 import remove_duplicates
#
# ph_number= "123@2344@46565757@33"
# d={}
# def count(p):
#     for i in ph_number:
#         d[i] = d.get(i, 0) + 1
#     return d
#
# d1=count(ph_number)
# #print(d1)
#
# for k,v in d1.items():
#     print(k,v,end="")

#
# #
# # name="shiva kumar"
# #
# # print(name[:-1].upper())
#
#
# def add_(*arg):
#     for i in arg:
#         print((i))
#
#
#
#
#
# add_(2,3,4,5,67,6,555,7)
# #
# # for i in range(5):
# #     for j in range(6):
# #         print(j,end="")
# #     print()
#
#
# # nums=[1,2,3,4,5]
# #
# # for i in nums:
# #     print(i)
# #
# # def arg(*agrs):
# #     for i in agrs:
# #         print(i,sep="-")
# #
# # arg(1,2,3,4,5,6,7,8,8)
#
#
# # nums= [1,2,3,4,-6,-5,-3,-4,6]
# #
# # pos= [num for num in nums if num >0]
# # print(pos,end=" ")
#
# res=lambda a,b:b*a*4
# print(res(1000,10))
#
# res1= lambda x:"even" if x%2==0 else "odd"
#
# print(res1(10))
#
# res2= lambda y: "pos"if y>0 else  "neg" if y<0 else "zero"
#
# print(res2(-22))
#
#
#
# # Creating a Tuple with repetition
# tup1 = ('Geeks',) * 3
# print(tup1)

# t1= ("shiva " )* 6
# print(t1,sep=" ")
#
# ph_number= "111112222333444555666"
#
# d={}
# for i in ph_number:
#     d[i]=d.get(i,0)+1
# #print(d)

#
# l=[1,2,2,5,5,6,]
# d2={}
# for j in l:
#     d2[j]=d2.get(j,0)+1
# print(d2)
#
# for k,v in d2.items():
#     if v==1:
#         print(k)
#
#
# import can
#
# bus= can.in



nums= [1,2,3,4,5]

# even=[i**2 for i in nums if i %2==0 ]
#
# print(even)
li=[]
for num in nums:
    if num%2==0:
        li.append(num**2)

    else:
        li.append(num**3)
print(li)

help(li)