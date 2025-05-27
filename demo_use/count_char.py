s="indiaa"
d={}
def count_char(a):
    for i in s:
        d[i]=d.get(i,0)+1
    print(d)
    for k,v in d.items():
        if v!=1:
            print(k)


count_char(s)

# s="innddia"
# seen=set()
# def repeated_char(s):
#     for i in s:
#         if i not in seen:
#             seen.add(i)
#         else:
#             print(i)
#             break
#
#
# repeated_char(s)