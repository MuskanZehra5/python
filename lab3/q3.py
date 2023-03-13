file_open = open('/Users/muskanzehra/PycharmProjects/lab3/alphabets.txt', 'r')

s = file_open.read()
x = s[::-1]
print(s)
print(x)

res_file = open('/Users/muskanzehra/PycharmProjects/lab3/out.txt', 'w')
res_file.write(x)

