# import sys
# # from collections import deque
# input = lambda: sys.stdin.readline().rstrip()
# n = int(input())
# house = [list(map(int, input().split()))for _ in range(n)]
# # q = deque()
# d = {0:[[0, 1, 0], [1, 1, 2]], 1: [[1, 0, 1], [1, 1, 2]], 2: [[1, 0, 1], [0, 1, 0], [1, 1, 2]]}
# # q.append([0, 1, 0])
# count = 0
# # visited = [[False for _ in range(n)]for _ in range(n)]
# # while q:
# #     x, y, direction = q.popleft()
# #     visited[x][y] = True
# #     for dir in d[direction]:
# #         nx = x + dir[0]
# #         ny = y + dir[1]
# #         if nx < 0 or ny < 0 or nx >= n or ny >= n:
# #             continue
# #         if visited[nx][ny]:
# #             continue
#         # if house[nx][ny] == 1:
#         #     continue
#         # if dir[2] == 2:
#         #     if house[nx-1][ny] == 1 or house[nx][ny-1] == 1:
#         #         continue
# #         if nx == n-1 and ny == n-1:
# #             count += 1
# #         q.append([nx, ny, dir[2]])
# # print(count)
# def dfs(x, y, way):
#     global count
#     for dir in d[way]:
#         print(dir)
#         nx = x + dir[0]
#         ny = y + dir[1]
#         if nx >= n or ny >= n:
#             return
#         if house[nx][ny] == 1:
#             return
#         if dir[2] == 2:
#             if house[nx-1][ny] == 1 or house[nx][ny-1] == 1:
#                 return
#         if nx == n-1 and ny == n-1:
#             count += 1
#             return
#         dfs(nx, ny, dir[2])
# dfs(0, 1, 0)
# print(count)
N = int(input())
house = []
for _ in range(N):
    house.append(list(map(int, input().split())))
total = 0


def dfs(x, y, direction):
    global total
    if x == N - 1 and y == N - 1 and house[x][y] == 0:
        total += 1
        return
    if direction == 0 or direction == 2:
        if y  < N - 1:
            if house[x][y + 1] == 0:
                dfs(x, y + 1, 0)
    if direction == 1 or direction == 2:
        if x < N - 1:
            if house[x + 1][y] == 0:
                dfs(x + 1, y, 1)
    if direction == 0 or direction == 1 or direction == 2:
        if x < N - 1 and y < N - 1:
            if house[x + 1][y] == 0 and house[x][y + 1] == 0 and house[x + 1][y + 1] == 0:
                dfs(x + 1, y + 1, 2)


dfs(0, 1, 0)
print(total)