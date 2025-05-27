names=input("enter")
words=names.split(",")
print(words)
d={}
for word in words:
    d[word]=d[word]+1
print(d)
