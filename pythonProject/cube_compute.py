def cube(num):
    for i in range(1, num + 1):
        print("Cube of {} is {}".format(i, i ** 3))


x = input('Enter a number : ')
cube(x)
