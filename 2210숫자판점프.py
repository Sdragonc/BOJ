import sys
from collections import deque
input= lambda: sys.stdin.readline().rstrip()
board = [list(map(int, input().split()))for _ in range(5)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
pos = dict()
for i in range(5):
    for j in range(5):
        q = deque()
        q.append([i, j, str(board[i][j]), 1])
        while q:
            x, y, s, cnt = q.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y  + dy[k]
                if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
                    continue
                if cnt == 5:
                    try:
                        pos[int(s+str(board[nx][ny]))]
                    except:
                        pos[int(s+str(board[nx][ny]))] = 1
                else:
                    q.append([nx, ny, s+str(board[nx][ny]), cnt+1])
print(len(pos.keys()))