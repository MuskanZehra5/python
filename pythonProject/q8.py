# Display numbers divisible by any number from a list

def divisibility(list_, n):
    print("The numbers divisible by {} are : ".format(n))
    for x in list_:
        if x % n == 0:
            print(x),
        else:
            pass


lst = []
y = int(input("Enter Number : "))
print("Enter list elements : ")
for x in range(0, y):
    lst.append(int(input()))
divisibility(lst, y)
