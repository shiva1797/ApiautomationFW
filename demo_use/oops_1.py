# class Stu:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def cal_avg(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
#         print(self.name,"your avg is",sum/2)
#
# class jstu(Stu):
#     pass
#
# js=jstu("sji",92)
#
# js.cal_avg()
#
# s1=Stu("anitha",[10,10,10])
# s1.cal_avg()
#

a="aeebbccdd"
d={}
non_rep=None
for i in a:
    d[i]=d.get(i,0)+1


for j in a:
    if d[j]==1:
        non_rep=j
        break
print(j)



seen=set()
for char in a:
    if char in seen:
        first_repeated = char
        print(first_repeated)
        break
    else:
         seen.add(char)



