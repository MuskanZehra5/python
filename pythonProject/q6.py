# Create a new list from a two list using the following condition
# Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

def join_lists(l1, l2):
    l3 = []

    for i in range(len(l1)):
        if i % 2 == 0:
            pass

        else:
            l3.append(l1[i])

    for j in range(len(l2)):
        if j % 2 == 0:
            l3.append(l2[j])

        else:
            pass

    return l3


l1 = ['10', '20', '25', '30', '35']
l2 = ['40', '45', '60', '75', '90']

l3 = join_lists(l1, l2)
print(l3)
