from curses.ascii import isalpha

from curses.ascii import isalnum

str1="a man,can,make a,mistake"
#
# sentence=''.join([str1.lower() for s in str1 if s.isalnum()])
# print(sentence)
def is_palindrome(sentence):
    cleaned = ''.join([sentence.lower() for char in sentence if char.isalnum()])
    return cleaned == cleaned[::-1]

# Example usage
sentence = "A man, a plan, a canal: Panama"
print(is_palindrome(sentence))  # Output: True