#Find the maximum number in a list

max_lst = [1,263,584,474,7474848]

def find_max(lst):
    max_va=lst[0]
    for i in lst:
        if max_va<i:
            max_va=i
    print(max_va)

find_max(max_lst)


