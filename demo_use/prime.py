def prime_c(n):
    for i in range(2,n):
        if n%i==0:
            print(n)
            return False
    print(n)
    return True

print(prime_c(79))