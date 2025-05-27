l= [11,11,34,4,4,5,6,6,7,8]


s=set()

for i in l:
    if i in s:
        repeated_n=i
        print(repeated_n)
        break
    s.add(i)
#
l= [1,34,4,5,5,6,6,7,7,8,8]

d={}

for i in l:
    d[i]=d.get(i,0)+1
print(d)

for j in l:
    if d[j]==1:
        non_re=j
        print(non_re)
        break




s=set()
for k in l:
    if k in s:
        repeated=k
        print(repeated)
        break
    s.add(k)


a="aabbcdd"

d={}

def find_str_nums(a):
    for i in a:
        d[i] = d.get(i, 0) + 1
    return d

data=find_str_nums(a)

for j,k in data.items():
    print(k,j,end="",sep="")