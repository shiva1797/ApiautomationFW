# l=[]
#
# size= int(input("enter size"))
#
# for i in range(0,size):
#     l.append(int(input("enter n")))
# avg = sum(l)/size
# print(avg)

#
# d= {"a":"apple","o":"orange","b":"ball","c":"cat"}
# usr=input("str")
# if usr in d.keys():
#     print("present")
#     print(f"value {d[usr]}")
# else:
#     print("no not present")


d={"a":10,"b":10,"c":1}
val= 1
for i in d.values():
    val=val*i

print(val)

