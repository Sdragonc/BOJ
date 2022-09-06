import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
n, m, k = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
matrix = [[0 for _ in range(m)]for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    matrix[a-1][b-1] = 1
visited = [[False for _ in range(m)]for _ in range(n)]
max_cnt = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            if not visited[i][j]:
                q = deque()
                tempt_cnt = 0
                visited[i][j] = True
                q.append([i, j])
                while  q:
                    x, y= q.popleft()
                    #print(x, y)
                    tempt_cnt += 1
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx < 0 or ny < 0 or nx >= n or ny >= m:
                            continue
                        if visited[nx][ny]:
                            continue
                        visited[nx][ny] = True
                        if matrix[nx][ny] == 1:
                            q.append([nx, ny])
                if max_cnt < tempt_cnt:
                    max_cnt = tempt_cnt
print(max_cnt)

                        