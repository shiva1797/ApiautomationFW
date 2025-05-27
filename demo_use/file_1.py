# data= "hey i love dosa"
#
# file_path= "out_file"
#
# with open(file_path,"w") as file:
#     file.write(data)
#     print("created and wrote data")


#
# first_name= "shiva"
# last_name= "kumar"
# place= "bengaluru"
#
# print(f"I'm {first_name}{last_name} from {place}!..")
# n=int(input("enter n:"))
#
# res =("pos" if n>0 else "neg")
#
# print(res)

d ={
    "name": "kumari",
    "age": 21,
    "sex": "female",
    "details":
    {
        "place": "goa",
        "code": 562125
    }
}
d1={}
for key,val in d.items():
    if isinstance(val,dict):
        d2="".join(f"{key}{val}"for k,v in val.items())
        d1=(f"{key}{d2}")
    else:
        d1=(f"{key}{val}")

print(d1)




#print(d)
