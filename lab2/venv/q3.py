# For a given string s, create a new string such that it replaces some characters of the string with
# '@';. To replace, find the first character of the given string s. Now find all occurrences of this first
# character in the string and replace them with '@' . Do not change the first character itself.
# e.g. 'Ooogle'; create 'O@@gle'
# Assume that the string is length 1 or more and take care of the word case.
# Hint: s.replace(stra, strb) returns a version of string s where all instances of stra have been
# replaced by strb.

def replace_(string, stra_, strb_):
    s = string[1:].lower()

    res = string[:1] + s.replace(stra_, strb_)
    return res


# x = raw_input("Enter a string : ")
y = replace_('ooogle', 'g', '@')
print("After Replacement : {}".format(y))
