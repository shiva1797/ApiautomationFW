d={"a":21,"b":25,"c":31,"d":253}

f,s=0,0
ke=0

for k,v in d.items():
    #print(v)
    if f<v:
        f,s=v,f
    elif f>v>s:
        s=v
print(s)
print(f"max number key and max value='{s}'")

