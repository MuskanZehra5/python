num = 1234
res = []
for x in str(num):
    res.append(int(x))

print(res)

ans = res[0] + res[len(res)-1]
print(ans)

