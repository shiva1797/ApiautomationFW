d={"a":1,"b":2,"c":3}

d1={}

for k,v in d.items():
    d1[v]=k
print(d1)

l=[1,2,3,4,5,5,6,7,7,8,8,9,9]

d2={}

for i in l:
    d2[i]=d2.get(i,0)+ 1
print(d2)
