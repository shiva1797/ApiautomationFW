# L1 = [[1, 2, 3], [4, 5],[2,3,4,5]]
#
# res = [i for subset in L1 for i in subset]
#
# print(res)
#from curses.ascii import islower

# data = "abcdaa hssbbye"
# s1= set()
# res=[]
#
# for i in data:
#     if i in s1 and i!="":
#         res.append("_")
#     else:
#         res.append(i)
#         s1.add(i)
# res1= "".join(res)
# print(res1)
# #abcd__ hs_b__e

#
# list_data = ["Nissan", "maruti", "hyundai", "Volkswagen", "audi"]
#
# res=[i for i in list_data if i[0].islower()]
#
# print(res)


data = "abcdaa hssbbye"

def dup(s):
    l=[]
    se=set()
    for i in s:
        if i in se and i==" ":
            break
        l.append(i)
        se.add(i)

    re="".join(l)
    print(re)

dup(data)