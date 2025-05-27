a = "aaaabbbcccdddeeegggsssaaa"

seen_ele=set()
li=[]
def dupss(a):
    for i in a:
        if i not in seen_ele:
            seen_ele.add(i)
            li.append(i)
    return "".join(li)

print(dupss(a))