# Write a program to calculate the sum of series up to n term.
# For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690

def series_sum(terms):
    sum = 0
    num = 2
    for i in range(0, terms):
        print(num),
        sum = sum + num
        num = 10 * num + 2
    print("\nThe sum of series upto {} terms is \'{}\'".format(terms, sum))


x = input('Enter the Number of terms : ')
series_sum(x)
