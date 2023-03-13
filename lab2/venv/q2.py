# Create a string made of the first three and the last three characters of the original string s and
# return the new string, so 'intelligence'; creates 'intcne';. However, if the string length is less than 3,
# return instead the empty string.

ip = raw_input("Enter a string : ")

if len(ip) > 3:
    new_str = ip[0:3] + ip[-4:-1]
    print(new_str)

elif len(ip) == 3:
    new_str = ip
    print(new_str)

else:
    print("")
