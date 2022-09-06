import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
n, k, r = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
road = [[[] for _ in range(n)]for _ in range(n)]
for _ in range(r):
    r1, c1, r2, c2 = map(int, input().split())
    road[r1-1][c1-1].append([r2-1, c2-1])
    road[r2-1][c2-1].append([r1-1, c1-1])
cow_list = []
couple = 0
for i in range(k):
    x, y = map(int, input().split())
    cow_list.append([x-1, y-1])
for i, cow in enumerate(cow_list):
    q = deque()
    q.append([cow[0], cow[1]])
    visited = [[False for  _ in range(n)]for _ in range(n)]
    visited[cow[0]][cow[1]] = True
    while q:
        x, y = q.popleft()
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny]:
                continue
            if [nx, ny] in road[x][y]:
                continue
            q.append([nx, ny])
            visited[nx][ny] = True
    for h in cow_list[i+1:]:
        if not visited[h[0]][h[1]]:
            couple += 1
print(couple)