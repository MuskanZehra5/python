class Node:
    def __init__(self, state, l, f):
        self.data = state
        self.level = l
        self.fx = f

    def find_space(self, state):
        for i in range(0, 3):
            for j in range(0, 3):
                if state[i][j] == "*":
                    return i, j

    def swap_tiles(self, state, x1, x2, y1, y2):
        new_data = []
        # making a copy of parent state
        for i in state:
            temp_d = []
            for j in i:
                temp_d.append(j)
            new_data.append(temp_d)
        # swapping values
        temp = new_data[x1][y1]
        new_data[x1][y1] = new_data[x2][y2]
        new_data[x2][y2] = temp

        return new_data

    # xs, ys = value of space
    def move_tiles(self, state, xs, x2, ys, y2):

        if 0 <= x2 < 3 and 0 <= y2 < 3:
            return self.swap_tiles(state, xs, x2, ys, y2)
        else:
            return None

    def childrens(self):
        x, y = self.find_space(self.data)
        dire_s = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        children = []

        for i in dire_s:
            child = self.move_tiles(self.data, x, i[0], y, i[1])
            if child is not None:
                c_node = Node(child, self.level + 1, 0)
                children.append(c_node)

        return children


def heuristic(initial, goal):
    heu = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if initial[i][j] != '*' and initial[i][j] != goal[i][j]:
                heu += 1

    return heu


def f_x(initial, goal):
    # fx = gx + hx
    f = initial.level + heuristic(initial.data, goal)
    return f


def print_matrix(data):
    for i in data:
        for j in i:
            print(j, end=" ")

        print("")

    print("")


if __name__ == '__main__':
    initial = []
    print("INITIAL STATE")
    print("Enter numbers from 0-8 with blank = *")
    for i in range(0, 3):
        num = input("Enter rows separated by space(*): ").split(" ")
        initial.append(num)

    goal = []
    print("GOAL STATE")
    for i in range(0, 3):
        num = input("Enter row # " + str(i + 1) + " separated by space(*) : ").split(" ")
        goal.append(num)

    # making initial state a node
    initial_s = Node(initial, 0, 0)
    initial_s.fx = f_x(initial_s, goal)

    main_list = [initial_s]
    closed = []
    no_of_moves = 0

    while True:
        current = main_list[0]

        print("   --- >   ")
        no_of_moves += 1

        print_matrix(current.data)

        if heuristic(current.data, goal) == 0:
            break

        many_C = current.childrens()

        for i in many_C:
            i.fx = f_x(i, goal)
            main_list.append(i)

        closed.append(current)
        del main_list[0]

        main_list.sort(key=lambda val: val.fx, reverse=False)

    print("Number Of Moves : " + str(no_of_moves - 1))

# init      #goal
# 1 2 5     #* 1 2
# 3 4 *     #3 4 5
# 6 7 8     #6 7 8


# init      #goal    #goal
# 1 * 2     1 2 4    1 6 2
# 7 5 4     7 6 5    7 3 4
# 8 6 3     8 3 *    * 8 5


