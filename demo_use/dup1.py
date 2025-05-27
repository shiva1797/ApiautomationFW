d ="aabbcd"
see=set()
l=[]
def dup1(d):
    for i in d:
        if i not in see:
            see.add(i)
            l.append(i)

    return "".join(l)



print(dup1(d))

# word="apple"
#
# res=""
#
# for i in word:
#     res=i+res
# print(res)
#
# d = {1: 'Geeks', 2: 'For', 'age':22}
#
# for k,v in d.items():
#     print(v)
#
