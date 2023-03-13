# find factorial of a given number

def factorial(num):
    res = 1
    for i in range(1, num + 1):
        res = res * i

    return res


x = input('Enter a number : ')
res = factorial(x)
print("Factorial of {} is {}".format(x, res))