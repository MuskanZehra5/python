set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 5, 7}

u = set1.union(set2)
i = set1.intersection(set2)

res = u.difference(i)

print(set1)
print(set2)
print(res)


