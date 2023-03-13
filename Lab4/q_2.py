from collections import deque

que = deque()

que.append('eat')
que.append('code')
que.append('sleep')
que.append('repeat')

print("Original Queue : ", que)

que.pop()


print("After Lifo pop : ", que)
