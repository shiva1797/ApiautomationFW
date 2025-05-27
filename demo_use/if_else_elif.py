# age=1
# if age>12:
#     print("permitted")
# elif age<12:
#     print("no permission")
# else:
#     print("nothing")
#
# c=1
# while c<10:
#     print(c)
#     c+=1
#

for i in range(1,5):
    for j in range(i):
        print(i,end=' ')
    print()

# for i in range(1, 5):
#     for j in range(i):
#         print(i, end=' ')
#     print()

def is_true(a):
    return bool(a)

print(is_true(5<10))


