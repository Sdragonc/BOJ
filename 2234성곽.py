import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
m, n = map(int, input().split())
#a = format(15, 'b')
wall = [[[0, 0, 0, 0]for _ in range(m)]for _ in range(n)]
input_mtr = [list(map(int, input().split()))for _ in range(n)]
for i in range(n):
    for j in range(m):
        binary = format(input_mtr[i][j], 'b')
        for k in range(len(binary)-1, -1, -1):
            if binary[len(binary)-k-1] == '1':
                wall[i][j][k] = 1
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
visited = [[False for _ in range(m)]for _ in range(n)]
wall_visited = [[[False for _ in range(4)] for _ in range(m)]for _ in range(n)]
max_room = 0
wall_break_max = 0
room_num = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]: #벽을 부수지 않았을 떄 방 갯수와 최대 크기
            q = deque()
            q.append([i, j])
            visited[i][j] = True
            tempt_area = 1
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        continue
                    if wall[x][y][k] == 1:
                        continue
                    if visited[nx][ny]:
                        continue
                    q.append([nx, ny])
                    visited[nx][ny] = True
                    tempt_area += 1
            if max_room < tempt_area:
                max_room = tempt_area
            room_num += 1
        break_flag= False
        wall_break_visited = [[False for _ in range(m)]for _ in range(n)]
        wall_break_visited[i][j] = True
        tempt_break_area = 1
        q = deque()
        q.append([i, j])
        while q:
            x, y = q.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx< 0 or ny <0 or nx>=n or ny >= m:
                    continue
                if not wall_break_visited[nx][ny]:
                    if wall[x][y][k] == 1:
                        if not break_flag:
                            if not wall_visited[x][y][k]:
                                    wall_visited[x][y][k] = True
                                    break_flag = True
                                    q.append([nx, ny])
                                    wall_break_visited[nx][ny] = True
                                    tempt_break_area +=  1
                    else:
                        q.append([nx, ny])
                        wall_break_visited[nx][ny] = True
                        tempt_break_area +=  1
        if wall_break_max < tempt_break_area:
            wall_break_max = tempt_break_area
print(room_num, max_room, wall_break_max, sep="\n")