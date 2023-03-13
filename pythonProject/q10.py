# Return the count of a given substring from a string

def count_substring(string, sub):
    x = string.count(sub)
    print("The word \'{}\' appeared {} times in the String".format(sub, x))


string = str(raw_input("Enter your String : "))
sub = str(raw_input("Enter Substring : "))
count_substring(string, sub)