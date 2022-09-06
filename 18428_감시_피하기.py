import sys
from itertools import combinations
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
passage = [list(input().split())for _ in range(n)]
blank = []
teacher = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(n):
    for j in range(n):
        if passage[i][j] == 'X':
            blank.append([i, j])
        elif passage[i][j] == 'T':
            teacher.append([i, j])
possibility = list(combinations(blank, 3))
flag = False
for pos in possibility:
    #print(pos)
    new_mtr = [[passage[i][j]for j in range(n)]for i in range(n)]
    spotted = False
    for p in pos:
        new_mtr[p[0]][p[1]] = 'O'
    # for k in range(n):
    #     for h in range(n):
    #         print(new_mtr[k][h], end = ' ')
    #     print()
    for t in teacher:
        for i in range(4):
            nx, ny = t
            while True:
                nx += dx[i]
                ny += dy[i]
                #print(nx, ny)
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    break
                if new_mtr[nx][ny] == 'O':
                    break
                if new_mtr[nx][ny] == 'S':
                    spotted = True
                    break
            if spotted:
                break
        if spotted:
            break
    if not spotted:
        flag = True
        break
if flag:
    print('YES')
else:
    print('NO')
