input_string = "abcabcbb dabbcgg xzm   "
seen=set()
li=[]
def remove_dup(input):
    for i in input_string.strip():
        if i not in seen and i!=" ":
            seen.add(i)
            li.append(i)
    res="".join(li)
    return res

print(remove_dup(input_string))


