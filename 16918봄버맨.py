import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
r, c, n = map(int, input().split())
mtr = [input() for _ in range(r)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
bomb = [[mtr[i][j] for j in range(c)]for i in range(r)]
cnt = 1
if n == 1:
    for i in range(r):
        for j in range(c):
            print(bomb[i][j], end = '')
        print()
else:
    if n % 2 == 0:
        for i in range(r):
            for j in range(c):
                print('O', end = '')
            print()
    else:
        for i in range(n//2):
            ans = [["O" for _ in range(c)] for _ in range(r)]
            for j in range(r):
                for k in range(c):
                    if bomb[j][k] == 'O':
                        ans[j][k] = '.'
                        for h in range(4):
                            nx = j + dx[h]
                            ny = k + dy[h]
                            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                                continue
                            if ans[nx][ny] == 'O':
                                ans[nx][ny] = '.'
            for j in range(r):
                for k in range(c):
                    bomb[j][k] = ans[j][k]
        for i in range(r):
            for j in range(c):
                print(ans[i][j], end = '')
            print()