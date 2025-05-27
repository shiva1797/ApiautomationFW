# list_data = ["NISSAN", "maruti", "hyundai", "Volkswagen", "audi"]
#
# for data in list_data:
#
#     if data == data.upper():
#         print(data)


data = "abcdaa hssbbye"
s = set()
result = []

for i in data:
    if i in s and i != " ":
        result.append("_")
    else:
        result.append(i)
        s.add(i)

output = "".join(result)
print(output)


print("shiva","kumar",end="  ")


