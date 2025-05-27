# l1 =[1,2,3,4,5,6,7,8]
#
# def print_lst(lst):
#
#     for item in l1:
#
#         print(item,end="")
#
# print_lst(l1)

def rec(n):
    if(n==11):
        return
    print(n)
    rec(n+1)

rec(1)