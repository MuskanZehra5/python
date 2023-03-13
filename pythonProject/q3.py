# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

def exponent(base, exp):
    res = base

    for i in range(0, exp-1):
        res = res * base

    return res


print("Enter base and exponent : ")

b = input("Base : ")
e = input("Exponent : ")

x = exponent(b, e)

print("{} raises to the power of {} : {}".format(b, e, x))
