s="shiva"

def check_polindrome(s):
    l,r=0,len(s)-1

    while l<r:
        if s[l].lower()!=s[r].lower():
            return False
        l,r=l+1,r-1
    return True



print(check_polindrome(s))