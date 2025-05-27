s="shiva"
s1="vashc"

def check_ana(s1,s2):
    d1,d2={},{}
    if len(s1)!=len(s2):
       return False
    for i in range(len(s2)):
        d1[s1[i]]=d1.get(s1[i],0)+1
        d2[s2[i]]=d2.get(s2[i],0)+1
    print(d1,d2)
    for k in d1:
        if d1[k]!=d2.get(k,0):
            return False
    return True
print(check_ana(s,s1))

