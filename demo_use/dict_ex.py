# data = {
#     'key1': 56,
#     'key2': 45,
#     'key3': [1, 2, 3, 9, 5],
#     'key4': 'ABC'
# }

# Check if any key has a list as value and if all elements in the list are integers
#for key, value in data.items():

data = {
        'key1': 56,
        'key2': 45,
        'key3': [1, 2, 3, 9, 5],
        'key4': 'ABC'
    }


    # Function to check if a value behaves like a list
def is_list(value):
        try:
            l = value[0]  # Lists support indexing
            value.append(value[-1])  # Lists support append()
            value.pop()  # Restore original value
            return True
        except (TypeError, AttributeError, IndexError):
            return False


    # Checking keys
for key, value in data.items():
        if is_list(value):
            print(f"Key '{key}' has a list as its value: {value}")



k=[1, 2, 3, 9, 5,"s"]

for i in k:
    if type(i)==str:
        print("int",i)
        break





