# def find_max(lst):
#     max_val = float('-inf')
#
#     for item in lst:
#         if isinstance(item, list):
#             max_val = max(max_val, find_max(item))
#         else:
#             max_val = max(max_val, item)
#
#     return max_val
#
# l = [1, 2, 3, [4, [5, 6, 7], 9, 6]]
# print(find_max(l))  # Output: 9i




# def find_max_num(l):
#     max_val=0
#     for i in l:
#         if isinstance(i,list):
#             max_val=max(max_val,find_max_num(i))
#         else:
#             max_val=max(max_val,i)
#     return max_val
#
# l=[1,2,3,4,[5,[5,6,7,7,8,866],66,77]]
#
# print(find_max_num(l))

#
# def flatten_list(lst):
#     flat_list = []
#     for item in lst:
#         if isinstance(item, list):
#             flat_list.extend(flatten_list(item))  # Recursively flatten sublists
#         else:
#             flat_list.append(item)
#     return flat_list
# l = [1, 2, 3, [4, [5, 6, 7], 9, 6]]
# flattened = flatten_list(l)
# print(flattened)
def flat_list(l):
    flat_l=[]
    for i in l:
        if isinstance(i,list):
            flat_l.extend(flat_list(i))
        else:
            flat_l.append(i)
    return flat_l
l = [1, 2, 3, [4, [5, 6, 7], 9, 6]]
print(flat_list(l))







