l="sshhivakumar"

def check_count(l):
    d={}
    for i in l:
        d[i]=d.get(i,0)+1
    print(d)
    for k,v in d.items():
        if v!=1:
            pass
        else:
            print(k)




check_count(l)