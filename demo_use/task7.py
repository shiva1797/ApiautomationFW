d1 ={"name": "shiva","age": 20,"colg":{  "city": "bang"  }
}
#print(d1.values())
#print(d1.keys())
#print(list(d1.items()))
# dic_res={}
# tup = ()
# lst =[]
#
# print(type(dic_res))
# print(type(tup))
# print(type(lst))

for k,v in d1.items():
    if isinstance(v,dict):
        sub_dic="".join(f"{k},{v}" for ke,val in v.items())
        dic_res=(f"{k}{sub_dic}")

    else:
        dic_res= (f"{k}{v}")

print(dic_res)
