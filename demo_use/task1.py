lst = [2, 5, 6, 7, 8, 'A', 'B', 'C', 9, 1]

# Filter out non-integer values
res=[val for val in lst if isinstance(val,int)]
print(res)

#even_num = [i for i in res if i%2==0]
#odd_num = [i for i in res if i%2!=0]


#a = [2,3,4,5]

#res1 = [i*2 for i in a]

#res2 =["even" if i%2 ==0 else "odd" for i in a]

#print(res2)

#print(res1)
