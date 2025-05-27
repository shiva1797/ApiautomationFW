l=[1,2,6,7,3,4,5]

s=set()
def check_dup(l):
    for i in l:
        if i in s:
            print(i)
            return True
        s.add(i)
    print(s)
    return False


print(check_dup(l))



