l= [1,11,43,1,77]

def sec_max(l):
    first,second=float("-inf"),float('-inf')

    for num in l:
        if num > first:
            second,first= first,num

        elif num>second<first:
            second =num
    return second


print(sec_max(l))


# def second_highest(numbers):
#     first, second = float('-inf'), float('-inf')
#     for num in numbers:
#         if num > first:
#             second, first = first, num
#             print(second,first)
#         elif first > num > second:
#             second = num
#     return second if second != float('-inf') else None
# #
# nums = [10, 20, 5, 30, 30, 10]
# print(second_highest(nums))  # Output: 20

