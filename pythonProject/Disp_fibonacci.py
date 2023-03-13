# Display Fibonacci series up to n terms

def fibonacci(num):
    num1 = 0
    num2 = 1
    for i in range(0, num):
        print(num1),
        num3 = num2
        num2 = num1 + num2
        num1 = num3


x = input("Enter no of terms : ")
fibonacci(x)
