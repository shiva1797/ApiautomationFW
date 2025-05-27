import keyword

n=1010101010100


def check_last_bit(n):
    res=n%2
    if res==1:
        return True
    return False

#
# print(check_last_bit(n))
#
#
#
# print(keyword.kwlist)
#

def count_up_to(n):
    count = 0
    while count <= n:
        yield count
        count += 1


for number in count_up_to(10):
    print(number)