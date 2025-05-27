# # Initial string
# s = "hello"
#
# # Store the original memory address
# original_id = id(s)
# print(original_id)
#
# # Try modifying the string (creates a new object)
# s = s + " world"
#
# # Store the new memory address
# new_id = id(s)
#
# # Check if the memory address changed
# print(f"Original ID: {original_id}")
# print(f"New ID: {new_id}")
#
# if original_id == new_id:
#     print("String is mutable")
# else:
#     print("String is immutable")


s="shiva"

org_id=id(s)

s=s+"kumar"

curr_id=id(s)

if org_id==curr_id:
    print(f"{org_id}=={curr_id}mutable")
print(f"{org_id} != {curr_id} immutable")