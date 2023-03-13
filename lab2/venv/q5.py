# Taking a list of strings as input, our matching function returns the count of the number of strings
# whose first and last chars of the string are the same.
# Also, only consider strings with length of 2 or more.


def count_func(string):
    string = string.lower()
    lst = string.split(" ")
    count = 0
    for i in lst:
        if i[0] == i[len(i)-1]:
            count += 1

    print(lst)
    print("The number of strings with same first and last character are : {}".format(count))


# x = raw_input("Enter A string : ")
count_func("apa banana Mango anna")
