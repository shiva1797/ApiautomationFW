# # Initializing variables
# a = "hello"
# b = 42
#
# # Asserting the type of a variable
# assert type(a) == str
# assert type(b) == int
#
# cnt = 2
# while (cnt <= 10):
#     if cnt%2==0:
#         #print(cnt)
#     cnt+=1
from demo_use.check_anagram import check_ana

#
# list = ["geeks", "for", "geeks"]
#
# for i in range(len(list)):
#     print(list[i])
# #

#
# s=set()
# def dup(a):
#     for i in a:
#         if i in s:
#             return True
#         else:
#             s.add(i)
#     return False
# a = [5,5, 2,2, 3,3, 4, 5]
# print(dup(a))
#

#
#
# s=set()
#
# for i in a:
#     if i in s:
#         print(f"dup:{i}")
#
#     s.add(i)

# d={}
# def count(sss):
#     for i in a:
#         d[i]=d.get(i,0)+1
#     return d
#
# res=count(a)
# print(res)
# #
# # for k,v in res.items():
# #     if v==1:
# #         non_rep=k
# #         print(non_rep)
# #         break
#
# s=set()
#
# for j in res.keys():
#     if j in s:
#         print(j)
#     s.add(j)
#
#
#
# a="aaabbbcccdef"
#
# def countn(a):
#     d={}
#     for i in a:
#         d[i]=d.get(i,0)+1
#     return d
#
# d1=countn(a)
# print(d1)
#
#
# for j,k in d1.items():
#     if k==1:
#         print(j)
#         break
#     print(j)
#     break

#
# a="aaaaaabbbcccdef"
#
# d={}
#
# for i in a:
#     d[i]=d.get(i,0)+1
#
# print(d)
#
# for k,v in d.items():
#     if v==1:
#         print(k)
#         break
#     else:
#         print(k)
#
#
# list = ["geeks", "for", "geeks"]
#
# for i in list:
#     print(i)

#
#
# a = [5,5, 2,2, 3, 4, 5]
#
# d={}
#
# for i in a:
#     d[i]=d.get(i,0)+1
# print(d)
#
# for k,v in d.items():
#     if v !=1:
#         print(k)
#         break


# def prime(n):
#     if n<=2:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#         print(n)
#         return True
#
#
# print(prime(4))
#
# n=10
# assert type(n)==int,f"{n} Not valid float"


a = [2,3, 4,4,5]
seen=set()
def check_dup(a):
    for i in a:
        if i in seen:
            return True
        else:
            seen.add(i)
    return False


print(check_dup(a))

