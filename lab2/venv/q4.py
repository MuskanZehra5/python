# Create a new string with the help of two input strings a and b. The new string should be
# separated by a space b/w a and b. Also swap the first 2 chars of each string and return it.
# e.g.
# mix, pod; -> pox mid
# dog, dinner -> dig donner

def new_str(str1, str2):
    x = str1[:2]
    y = str2[:2]

    str1 = str1.replace(x, y, 1)
    str2 = str2.replace(y, x, 1)
    res = str1 + ' ' + str2
    print(res)


new_str('mix', 'pod')
new_str('dog', 'dinner')
