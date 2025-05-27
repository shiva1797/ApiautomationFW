a = [1,2,3,4,5,66,66]
# s=set()
# def dup(a):
#     for i in a:
#         if i in s:
#             return True
#         else:
#             s.add(i)
#     return False
#
# print(dup(a))

seen=set()
def check_dup(a):
    for i in a:
        if i in seen:
            return True
        seen.add(i)
    return False

print(check_dup(a))

