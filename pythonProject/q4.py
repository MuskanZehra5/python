# Print downward Half-Pyramid Pattern with Star

x = input("Enter number : ")

for i in range(x, 0, -1):
    for j in range(i, 0, -1):
        print("*"),

    print("")
