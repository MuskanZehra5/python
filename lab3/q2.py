def division(num1, num2):
    try:
        res = float(num1 ) / float(num2)
        print("Your result : {}".format(res))
    except ValueError:
        print("Give either in or float value")

    except ZeroDivisionError:
        print("Division by 0 not possible")


x = input("Enter First Number : ")
y = input("Enter Second Number : ")
division(x, y)
