# Write a program to print the following start pattern using the for loop
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

def pattern_print(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("*"),
        print("")

    for k in range(n, 0, -1):
        for j in range(0, k - 1):
            print("*"),
        print("")


x = input('Enter integer : ')
pattern_print(x)
