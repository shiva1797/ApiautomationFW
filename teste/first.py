def prime(n):
    for i in range(2,n):
        if i%n==0:
            return False

    return True

print(prime(3))

