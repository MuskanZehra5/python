from game2dboard import Board

start = None
path = []
checked = set()


# -----------------------UCS--------------------
def ucsAlgo(start, stop, new_path, mat):
    new_path = new_path + [start]
    if start == stop:
        return new_path
    shortest = None
    for i in mat[start]:
        if i not in new_path:
            track = ucsAlgo(i, stop, new_path, mat)
            if track:
                if not shortest or len(track) < len(shortest):
                    shortest = track
    return shortest


def ucs(st, stop, r, c, mat):
    new_path = []
    start = st
    path = ucsAlgo(start, stop, new_path, mat)
    new_grid = Board(r, c)
    new_grid.cell_size = 80
    new_grid.title = "UCS"
    new_grid.cell_color = "turquoise"
    new_grid.margin_color = 'yellow'
    new_grid.grid_color = 'yellow'

    origin = 1

    try:
        for i in path:
            for j in range(len(new_grid)):
                for k in range(len(new_grid[0])):
                    if i == (j, k):
                        new_grid[j][k] = origin
                        origin += 1
    except:
        print("No Possible Path By UCS")

    new_grid.show()


# -------------------BFS---------------------
def bfsAlgo(mat, st):
    checked.add(st)
    job_queue = [st]

    while job_queue:
        value = job_queue.pop(0)
        path.append(value)

        for next in mat[value]:
            if next not in checked:
                job_queue.append(next)
                checked.add(next)


def bfs(st, stop, r, c, mat):
    start = st
    bfsAlgo(mat, start)

    new_grid = Board(r, c)
    new_grid.cell_size = 80
    new_grid.title = "BFS"
    new_grid.cell_color = "turquoise"
    new_grid.margin_color = 'yellow'
    new_grid.grid_color = 'yellow'

    origin = 1
    x, y = 0, 0
    path1 = []

    try:
        while path[x] != stop:
            path1.append(path[x])
            x += 1
        path1.append(stop)

        for i in path1:
            for j in range(len(new_grid)):
                for k in range(len(new_grid[0])):
                    if i == (j, k):
                        new_grid[j][k] = origin
                        origin += 1
    except:
        print("No Possible Path By BFS")

    new_grid.show()


# ------------------DFS-----------------------------
def dfsAlgo(mat, st):
    if st not in checked:
        path.append(st)

        checked.add(st)
        for next in mat[st]:
            dfsAlgo(mat, next)


def dfs(st, stop, r, c, mat):
    start = st
    dfsAlgo(mat, start)

    x, y = 0, 0
    path1 = []

    try:
        while path[x] != stop:
            path1.append(path[x])
            x += 1
        path1.append(stop)

        for i in path1:
            for j in range(len(path1)):
                for k in range(len(path1[0])):
                    if i == (j, k):
                        print(j,k)


    except:
        print("No Possible Path By DFS")


# ----------------GREEDY---------------------------


def greedyAlgo(self,row, col, mat):
    visited = [[0] * col for _ in range(row)]
    size = row
    if (row == size - 1) and (col == self.size - 1):
        visited[row][col] = 1
        return True

    if 0 <= row < size and 0 <= col < size and visited[row][col] == 0 and mat[row][col] == 0:

        visited[row][col] = 1

        if greedyAlgo(row + 1, col) or greedyAlgo(row, col + 1) or greedyAlgo(row - 1, col) or greedyAlgo(row, col - 1):
            return True

        visited[row][col] = 0
        return False
    return 0


def greedy(self,start, stop, r, c, mat) -> None:
    if not greedyAlgo(0, 0, mat):
        print("No Possible Path By GREEDY ")
            return

    for j in range(len(self.visited)):
        for k in range(len(self.visited[0])):
            if self.visited[j][k] == 1:
                print(j,k)


if __name__ == '__main__':
    mat = [[0, 0, 0, 0, 0],
           [1, 0, 1, 0, 0],
           [0, 0, 1, 0, 0],
           [1, 0, 0, 1, 0]]

    row = len(mat)
    col = len(mat[0]) if row > 0 else 0
    graph = {(i, j): [] for j in range(col) for i in range(row) if not mat[i][j]}

    for r, c in graph.keys():
        if r < row - 1:
            if not mat[r + 1][c]:
                graph[(r, c)].append((r + 1, c))
                graph[(r + 1, c)].append((r, c))

        if c < col - 1:
            if not mat[r][c + 1]:
                graph[(r, c)].append((r, c + 1))
                graph[(r, c + 1)].append((r, c))

x = input("Select \n1) DFS \n2) BFS \n3) UCS \n4) GREEDY\n")

if x == '1':
    dfs((0, 0), (row - 1, col - 1), row, col, graph)

elif x == '2':
    bfs((0, 0), (row - 1, col - 1), row, col, graph)

elif x == '3':
    ucs((0, 0), (row - 1, col - 1), row, col, graph)

elif x == '4':
    greedy((0, 0), (row - 1, col - 1), row, col, graph)


else:
    print("Invalid Input")
