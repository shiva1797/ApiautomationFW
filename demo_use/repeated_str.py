data="abcabcbbdjhsghjgjhdiojuis"
#s= set()
l=[]
for i in data:
    if i not in l:
        l.append(i)
    res="".join(l)


print(res)

#
# x, y = input("Enter two values: ").split(",")
# print("Number of boys: ", x)
# print("Number of girls: ", y)


for i in range(5):
    for j in range(i):
        print(i ,end=" ")
    print()




