# data= "12345555333377774"
# li=[]
# seen=set()
# def rd(data):
#     for i in data:
#         if i not in seen:
#             seen.add(i)
#             li.append(i)
#         res="".join(sorted(li))
#     return res
#
# print(rd(data))
#
d1="shivakumar"
d={}
def check_char(d1):
    for i in d1:
        d[i]=d.get(i,0)+1

    return d

print(check_char(d1=d1))
print(help(check_char))
#
#
# for number in range(1,20):
#     if number %3 == 0 and number %5 == 0:
#         print("FIZZBUZZ")
#     elif number % 3 == 0:
#         print("FIZZ")
#     elif number % 5 == 0:
#         print("BUZZ")
#     else:
#         print(number)







