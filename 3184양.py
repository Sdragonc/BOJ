import sys
from collections import deque
input= lambda: sys.stdin.readline().rstrip()
r, c =map(int, input().split())
backyard = [input()for _ in range(r)]
q = deque()
visited = [[False for _ in range(c)]for _ in range(r)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = [0, 0]
for i in range(r):
    for j in range(c):
        if backyard[i][j] != '#' and not visited[i][j]:
            q = deque()
            q.append([i, j])
            count = [0, 0]
            if backyard[i][j] == 'o':
                count[0] += 1
            elif backyard[i][j] == 'v':
                count[1] += 1
            visited[i][j] = True
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or ny < 0 or nx >= r or ny >= c:
                        continue
                    if visited[nx][ny]:
                        continue
                    if backyard[nx][ny] == 'o':
                        count[0] += 1
                    elif backyard[nx][ny] == 'v':
                        count[1] += 1
                    if backyard[nx][ny] != '#':
                        q.append([nx, ny])
                        visited[nx][ny] = True
            #print(count)
            if count[0] > count[1]:
                ans[0] += count[0]
            else:
                ans[1] += count[1]
print(*ans, sep=' ')