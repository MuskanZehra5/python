# Write a program to remove characters from a string starting from zero up to n and return a new string.
# eg.remove_chars("pynative", 4) so output must be tive. Here we need to remove first four characters from a string.


def remove_char(string, n):
    res = string[n:]
    print("After removing first {} characters from \'{}\' the result is \'{}\' : ".format(n, string, res))


s = raw_input("Enter String : ")
n = input("Enter value of n : ")
remove_char(s, n)
