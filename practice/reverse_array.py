arr = [1,2,3,4,5]
res = []

for i in range(len(arr)):
    x = len(arr) - (i+1)
    res.append(arr[x])


print(res)
