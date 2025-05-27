def remove_duplicates(s):
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return "".join(result)

input_string = "abcabcbbdjhsghjgjhdiojuis"
output_string = remove_duplicates(input_string)
print("Output:", output_string)

