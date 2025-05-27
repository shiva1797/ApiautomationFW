word=("shivakumaramukavihs")
# shivakumaramukavihs
def check_polin(word):
    l,r=0,len(word)-1
    if word[l]!=word[r]:
        return False
    l,r=l+1,r-1
    return True


print(check_polin(word))

