#list flattening

L1 = [[1, 2, 3], [4, 5]]

res =[item for subset in L1 for item in subset]


print(res)

L1_flat = []
for sublist in L1:
    for item in sublist:
        L1_flat.append(item)
print(L1_flat)





# Write Python 3 code in this online editor and run it.
nested_list = [[1, 2, 3], [4, 5, 6]]
#print(nested_list[2][0])  # IndexError: list index out of range
#Solution: Ensure the index exists before accessing.
print(nested_list[0][0])


nested_list = [[1, 2], [3, 4], [5, 6]]
nested_list = [sublist for sublist in nested_list if not 5 in sublist]
print(nested_list)  # [[1, 2], [5, 6]]


nested_list = [[1, 2], [3, 4], [5, 6]]

res_list = [item for subset in nested_list for item in subset]

print(res_list)

print(any(3 in sublist  for sublist in nested_list))