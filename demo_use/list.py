# marks=[90,91,92,93,95,90,90]
#
# # for mark in marks:
# #     print(mark)
#
# cnt=marks.count(90)
# print(cnt)
# marks.append(99)
# print(marks)
#
# ind=marks.index(90)
# print(ind)
# marks.sort()
# print(marks)
#
# marks1=marks.copy()
# print(marks1)
# marks.reverse()
# print(marks)
#
# marks.extend([1,2,4,5,6])
# print(marks)
#
# marks.insert(0,100)
# print(marks)
#
# marks.remove(100)
# print(marks)
#
# marks.pop()
# print(marks)
#
# # marks.clear()
# #
# # print(marks)
# print(100 not in marks)
# print(len(marks))
#
#
# for num in marks:
#     if num==90:
#         continue
#     print(num)
#
#
# str="shiva"
# print("s" not in str)
#


list_data = ["Nissan", "maruti", "hyundai", "Volkswagen", "audi"]

res=[i for i in list_data if  i[0].islower()]

print(res)


