# Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.

def sum(num):
    if num:
        return sum(num - 1) + num
    else:
        return 0


x = input("Enter no of terms : ")
res = sum(x)
print("The sum upto {} terms is \'{}\'".format(x, res))
