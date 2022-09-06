import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
matrix = [list(map(int, input().split()))for _ in range(n)]
new = [[0 for _ in range(n)]for _ in range(n)]
cnt = 0
visited = [[False for _ in range(n)]for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            if not visited[i][j]:
                cnt += 1
                q = deque()
                q.append([i, j])
                visited[i][j] = True
                new[i][j] = -1
                while q:
                    x, y = q.popleft()
                    flag = False
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx < 0 or ny < 0 or nx >= n or ny >= n:
                            continue
                        if visited[nx][ny]:
                            continue
                        if matrix[nx][ny] == 0:
                            new[x][y] = cnt
                            flag = True
                        if matrix[nx][ny] == 1:
                            visited[nx][ny] = True
                            q.append([nx, ny])
                    if not flag:    
                        new[nx][ny] = -1
min_bri = 1e9
for i in range(n):
    for j in range(n):
        if new[i][j] != 0 and new[i][j] != -1:
            island = new[i][j]
            print(min_bri)
            tempt = 0
            q = deque()
            q.append([i, j, 0])
            visited = [[False for _ in range(n)]for _ in range(n)]
            visited[i][j] = True
            flag = False
            while q:
                x, y, cnt = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue
                    if visited[nx][ny]:
                        continue
                    if new[nx][ny] != 0 and new[nx][ny] != island and new[nx][ny] != -1:
                        tempt = cnt
                        flag = True
                        # if i == 4 and j == 3:
                        #     print(nx, ny)
                        break
                    if new[nx][ny] == 0:
                        q.append([nx, ny, cnt+1])
                        visited[nx][ny] = True
                if flag:
                    break
            if min_bri > tempt:
                min_bri = tempt
# print()
# for i in range(n):
#     for j in range(n):
#         print(new[i][j], end = ' ')
#     print()
print(min_bri)
