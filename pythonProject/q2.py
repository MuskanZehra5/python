# coding=utf-8
# Write a program to accept a string from the user and display characters that are present at an even
# index number. For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

def display_even(s):
    new = []
    st = " "
    for i in range(len(s)):
        if i % 2 == 0:
            new.append(s[i])
            print("\'{}\'".format(s[i]))

    print(new)


s = 'pynative'
display_even(s)
