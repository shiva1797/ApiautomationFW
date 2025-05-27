dic = {"k1": "v1", "k2": {"k21": "v21"}, "k3": "v3"}

result = []
for i ,j in dic.items():
    if isinstance(j,dict):
        #print(j)


        result.append(f"{i}{j}")


print(result)


