import random
lst = [random.randint(-15,15) for i in range(10)]
print(lst)

lst_ans = list(map(lambda x :x**2,lst))
print(lst_ans)

#OUTPUT:
# [-4, 1, -10, 15, -12, 8, -14, 12, -2, -3]
# [16, 1, 100, 225, 144, 64, 196, 144, 4, 9]