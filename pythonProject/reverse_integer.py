# reverse an integer number

def reverse(num):
    print('Number :' + str(num))
    string = str(num)
    y = string[::-1]
    print("Reversed : " + y)


x = input('Enter a number : ')
reverse(x)
