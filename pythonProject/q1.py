# Write a Python program to replace a string "Python" with "Java" and "Java" with "Python" in a given string.

def replace(s):
    st = str(s)
    x = st.split()
    for i in range(len(x)):
        if "python" in x[i]:
            x[i] = "java"
        elif "java" in x[i]:
            x[i] = "python"

    print("Old string :" + st)

    print("After replacement new string :")
    new = " "
    new = ' '.join(x)
    print(new)


s = raw_input("Enter String :")
replace(s)
