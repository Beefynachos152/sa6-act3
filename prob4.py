list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

intersect = list(filter(lambda x: x in list1, list2))
print(intersect)
