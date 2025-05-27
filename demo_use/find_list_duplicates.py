
def check_dup(d):
    d = {}
    l = [1, 2, 3, 3, 4, 5]
    for i in l:
        d[i] = d.get(i, 0) + 1
    for k, v in d.items():
        if v == 1:
            return False
        else:
            return True


print(check_dup(d))