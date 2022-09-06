import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
dx = [[1, -1], [1, -1], [1, -1], [0, 0]]
dy = [[1, -1], [-1, 1], [0, 0], [1, -1]]
board = [list(map(int, input().split()))for _ in range(19)]
black_win = False
white_win = False
for i in range(19):
    for j in range(19):
        if board[i][j] != 0:
            for k in range(4):
                cnts = 0 
                ans = [[i, j]] 
                for h in range(2):
                    cnt = 1
                    flag = False      
                    nx = i + dx[k][h]
                    ny = j + dy[k][h]
                    #print(nx, ny)
                    if nx < 0 or ny < 0 or nx >= 19 or ny >= 19:
                        cnts += cnt
                        continue
                    if board[nx][ny] == board[i][j]:
                        cnt += 1
                        ans.append([nx, ny])
                        while True:
                            nx += dx[k][h]
                            ny += dy[k][h]
                            if nx < 0 or ny < 0 or nx >= 19 or ny >= 19:
                                cnts += cnt
                                flag = True
                                break
                            if board[nx][ny] == board[i][j]:
                                cnt += 1
                                ans.append([nx, ny])
                            else:
                                cnts += cnt
                                flag = True
                                break
                    else:
                        cnts += cnt
                    #print(cnts)
                cnts -= 1
                if cnts == 5:
                    if board[i][j] == 1:
                        black_win = True
                        break
                    else:
                        white_win = True
                        break
            if black_win or white_win:
                break
    if black_win or white_win:
        break
#print(ans)
if black_win:
    ans.sort(key = lambda x: [x[1], x[0]])
    print(1)
    print(ans[0][0]+1, ans[0][1]+1)
elif white_win:
    ans.sort(key = lambda x: [x[1], x[0]])
    print(2)
    print(ans[0][0]+1, ans[0][1]+1)
else:
    print(0)