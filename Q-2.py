lst1 = [1,2,3,4,5,6]
lst2 = [6,5,4,3,2,1]

lst = list(map(lambda x,y :x+y ,lst1,lst2))
print(lst)

#OUTPUT:
# [7, 7, 7, 7, 7, 7]