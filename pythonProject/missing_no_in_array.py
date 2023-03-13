# Write a Python program to find the missing number in a given array of numbers between 10 and 20.

def missing_num():
    ip = [11, 12, 13, 14, 15, 16, 19, 17]
    ip.sort()
    k = 10
    for j in range(0, 10):

        if ip.__contains__(k):
            k += 1

        else:
            print(k)


missing_num()
