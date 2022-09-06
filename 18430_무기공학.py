import sys
input = lambda: sys.stdin.readline().rstrip()
dx = [[1, 0], [-1, 0], [-1, 0], [1, 0]]
dy = [[0, -1], [0, -1], [0, 1], [0, 1]]
m, n = map(int, input().split())
wood = [list(map(int, input().split()))for _ in range(n)]
visited = [[False for _ in range(m)]for _ in range(n)]
max_hardness = 0
if (n <= 2 and m == 1) or (n == 1 and m <= 2):
    print(0)
elif n == 2 and  m == 2:
    for i in range(n):
        for j in range(m):
            tempt_hardness = 0
            for k in range(4):
                nx = i + dx[k][0]
                ny = j + dy[k][1]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    break
                tempt_hardness += wood[i][j]*2
                tempt_hardness += wood[nx][ny]
            if max_hardness < tempt_hardness:
                max_hardness = tempt_hardness
    print(max_hardness)
else:
    for i in range(n):
        for j in range(m):
            visited[i][j] = True
            for a in range(4):
                    tempt_hardness1 = 0
                    nx1 = i + dx[a][0]
                    ny1 = j + dy[a][0]
                    if nx1 < 0 or ny1 < 0 or nx1 >= n or ny1 >= m:
                        continue
                    nx2 = i + dx[a][1]
                    ny2 = j + dy[a][1]
                    if nx2 < 0 or ny2 < 0 or nx2 >= n or ny2 >= m:
                        continue
                    print(i, j, nx1, ny1, nx2, ny2)
                    tempt_hardness1 += wood[i][j]*2
                    tempt_hardness1 += wood[nx2][ny2]
                    tempt_hardness1 += wood[nx1][ny1]
                    visited[nx1][ny1] = True
                    visited[nx2][ny2] = True
                    for k in range(i, n):
                        for h in range(j, m):
                            for b in range(4):
                                tempt_hardness2 = 0
                                nnx1 = k + dx[b][0]
                                nny1 = h + dy[b][0]
                                if nnx1 < 0 or nny1 < 0 or nnx1 >= n or nny1 >= m:
                                    continue
                                if visited[nnx1][nny1]:
                                    continue
                                nnx2 = k + dx[b][1]
                                nny2 = h + dy[b][1]
                                if nnx2 < 0 or nny2 < 0 or nnx2 >= n or nny2 >= m:
                                    continue
                                if visited[nnx2][nny2]:
                                    continue
                                tempt_hardness2 += wood[nnx2][nny2]
                                tempt_hardness2 += wood[nnx1][nny1]
                                tempt_hardness2 += wood[k][h]*2
                                tempt_hardness = tempt_hardness1 + tempt_hardness2
                                if max_hardness < tempt_hardness:
                                    max_hardness = tempt_hardness
                    visited[nx1][ny1], visited[nx2][ny2] = False, False       
            visited[i][j] = False
    print(max_hardness)