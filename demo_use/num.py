
data = "abcdaa hssbbye"
s = set()
result = []

for i in data:
    if i in s and i != " ":
        result.append("_")
    else:
        result.append(i)
        #s.add(i)

