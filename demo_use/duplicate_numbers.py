def dup_el(l):
    seen=set()
    for i in l:
        if i in seen:
            return i
        else:
            seen.add(i)
    return False



l=[1,2,4,5,6,7]
print(dup_el(l))







