import sys
import copy
input = lambda: sys.stdin.readline().rstrip()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n = int(input())
visited = [[False for _ in range(n)]for _ in range(n)]
board = [list(map(int, input().split()))for _ in range(n)]
max_candy = 0
for i in range(n):
    for j in range(n):
        color = board[i][j]
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[l]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny]:
                continue
            if board[nx][ny] != color:
                tempt_candy = 0
                tempt_board = copy.deepcopy(board)
                tempt_board[nx][ny], tempt_board[i][j] = tempt_board[i][j], tempt_board[nx][ny]
                if k == 0 or k == 1:
                    