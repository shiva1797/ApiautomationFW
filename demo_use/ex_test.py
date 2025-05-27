# value1=10 EUR
#value2=39 USD


#
# class ConverRS:
#     d={"usd":85,"eur":18}
#     for val in d.values():
#
#
#        def __init__(self,value,currency):
#         self.value= value
#         self.currency = currency
#
#
#        def convert_rs(self):
#             if self.currency in self.d:
#                 self.value = int(self.value * self.d[self.currency])
#                 print(f"converted value:RS {self.value}")
#             else:
#                 print(f"invalid currency{self.currency}")
#
#
#
# conv_obj = ConverRS(39,"usd")
#
# conv_obj.convert_rs()
#
#
#
#
#
# l= [1,2,3,4,5,6,7,9,8]
#
#
# def max_num(l):
#     max_val =l[0]
#     second_max = 0
#     for i in l:
#         if max_val <i and second_max>i:
#             second_max= max_val
#
#     print(second_max)
#
#
# max_num(l)



class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __repr__(self):
        return f"Student {self.name} grade {self.grade}"


classroom = [Student('Max Payne', 7), Student('Wynona Rider', 4), Student('Brad Pitt', 9)]
print(classroom)
classroom.sort(key=lambda p: p.grade)
print(classroom)

#sorted_list = sorted(person.mentees, key=lambda p: p.name)





