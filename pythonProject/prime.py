# Write a program to display all prime numbers within a range

def disp_prime(start, end):
    print("The prime numbers between {} and {} are :".format(start, end))
    for i in range(start, end + 1):
        count = 0
        for j in range(1, i):
            if i % j == 0:
                count += 1
            else:
                pass

        if count <= 1:
            print(i)


start = input("Enter 1st range : ")
end = input("Enter 2nd range : ")
disp_prime(start, end)
