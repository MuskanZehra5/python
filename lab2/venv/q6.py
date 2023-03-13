# Given a list of non-empty tuples, return a list sorted in increasing order by the last element in
# each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] creates [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.
def order_list(lst):
    lst.sort(key=lambda last: last[-1], reverse=False)
    print(lst)


x = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
print(x)
order_list(x)

# y = order_list(x)
# print(y)
