import sys
from collections import deque
from itertools import combinations
input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
institution = [list(map(int, input().split()))for _ in range(n)]
keneng = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 1e9
for i in range(n):
    for j in range(n):
        if institution[i][j] == 2:
            keneng.append([i, j])
poss = list(combinations(keneng, m))
#print(poss)
for pos in poss:
    q = deque()
    visited = [[False for _ in range(n)]for _ in range(n)]
    tempt_mtr = [[-1 for _ in range(n)]for _ in range(n)]
    for p in pos:
        q.append(p)
        tempt_mtr[p[0]][p[1]] = 0
        visited[p[0]][p[1]] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >=n or ny >= n:
                continue
            if visited[nx][ny]:
                continue
            if institution[nx][ny] != 1:
                tempt_mtr[nx][ny] = tempt_mtr[x][y] + 1
                q.append([nx, ny])
                visited[nx][ny] = True
    t = 0
    # for i in range(n):
    #     for j in range(n):
    #         print(tempt_mtr[i][j], end = ' ')
    #     print()
    # print()
    flag = False
    for i in range(n):
        for j in range(n):
            if institution[i][j] != 1:
                if tempt_mtr[i][j] == -1:
                    flag = True
                    break
                if institution[i][j] == 2:
                    continue
                if t < tempt_mtr[i][j]:
                    t = tempt_mtr[i][j]
        if flag:
            break
    if not flag:
        if answer > t:
            answer = t
print(answer) if answer != 1e9 else print(-1)