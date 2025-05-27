
a = [2,3, 4, 5,8,9,00,66,7,88,99,77]
seen=set()
def check_dup(a):
    for i in a:
        if i in seen:
            print(i)
            return True
        else:
            seen.add(i)
    print(seen)
    return False

print(check_dup(a))
