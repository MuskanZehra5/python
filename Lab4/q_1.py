def square_cube(lst):
    for element in lst:
        sq = lambda x: x ** 2
        cube = lambda x: x ** 3

        print("Number : {} \n Square : {} \n Cube : {}".format(element, sq(element), cube(element)))
        print("")


lst = [1, 3, 5, 7, 9, 11]
square_cube(lst)
