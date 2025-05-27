x=["a","b","c","d"]
y=[1,2,3,4]

res= tuple(zip(x,y))
print(res)
res1= list(zip(x,y))
print(res1)

d={k:v for k,v in zip(x,y)}
print(d)

output = {}
for i in range(len(x)):
    output[x[i]] = y[i]

print(output)




