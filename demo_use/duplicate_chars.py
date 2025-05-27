# from math import floor
#
# d =("abcdabcd")
# s=set()
# def is_dup(d):
#     for i in d:
#         if i in s:
#             return True
#         s.add(i)
#         print(i,end=" " )
#     return False
#
# print(is_dup(d))
#
#
#
# for j in range(10,-2,-2):
#     print(j)
#
# #
# # n=11
# #
# # r= n//2
# # print(r)
# #
# # n1=11.3
# #
# #
# # d={1:2,3:4,5:6}
# #
# # print(d.get(3))
# # d[1]=10
# # print(d)
# # d.update({1:9})
# # print(d)
# #
# # x=10
# #
# # res2= lambda x: x*3
# #
# # print(res2(x))
# #
# # d3= dict({'x': 123, 'y': 354})
# #
# # for k,l in d3.items():
# #     print(k,l)
# # list = ["geeks", "for", "geeks"]
# #
# # for i in range(len(list)):
# #
# #     print(i,list[i])
#
#
# a = [1, 2, 3, 4]
#
# # Using custom function in "function" parameter
# # This function is simply doubles the provided number
# def double(val):
#   return val*2
#
# res = map(double, a)
# print(list(res))
#
#
# # s = ['1', '2', '3', '4']
# # res = map(int, s)
# # print(list(res))
#


d = {1: 'Geeks', 2: 'For', 'age':22}

# # Iterate over keys
# for key in d:
#     print(key)
#
# # Iterate over values
# for value in d.values():
#     print(value)

# Iterate over key-value pairs
for key, value in d.items():
    if key ==2:
        print("yes")

    print("no")

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res= [i for i in mat for j in i]
print(res)




