li=[0,2,3,5,7,8,9,99,8]

def check_sec_large(li):
   f=s=float("-inf")
   for n in li:
       if n>f:
           f=n
           s=f
       elif f>n>s:
           s=n
   return s
print(check_sec_large(li))



