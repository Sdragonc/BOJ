import sys
input = lambda: sys.stdin.readline().rstrip()
r, c = map(int, input().split())
mtr = [list(input()) for _ in range(r)]
op = input()
dx = [1, 1, 1, 0, 0, 0, -1, -1, -1]
dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
jong = []
for i in range(r):
    for j in range(c):
        if mtr[i][j] == 'I':
            jong = [i, j]
            mtr[i][j] = -1
        elif mtr[i][j] == 'R':
            mtr[i][j] = 1
        else:
            mtr[i][j] = 0
flag = False
cnt = 0
for o in op:
    new_mtr = [[0 for _ in range(c)]for _ in range(r)]
    cnt += 1
    j_x = jong[0] + dx[int(o)-1]
    j_y = jong[1] + dy[int(o)-1]
    if mtr[j_x][j_y] == 1:
        flag = True
        break
    jong = [j_x, j_y]
    new_mtr[j_x][j_y] = -1
    for i in range(r):
        for j in range(c):
            if mtr[i][j] == 1:
                min_index  = -1
                min_val = 10000
                for k in range(9):
                    if k == 4:
                        continue
                    if min_val > abs(jong[0]-(i+dx[k])) + abs(jong[1]-(j+dy[k])):
                        min_val = abs(jong[0]-(i+dx[k])) + abs(jong[1]-(j+dy[k]))
                        min_index = k
        #print(cr[0], cr[1], min_index)
                if new_mtr[i+dx[min_index]][j+dy[min_index]] >= 1:
                    new_mtr[i+dx[min_index]][j+dy[min_index]]  += 1
                    continue
                elif new_mtr[i+dx[min_index]][j+dy[min_index]]  == -1:
                    flag = True
                    break
                else:
                    new_mtr[i+dx[min_index]][j+dy[min_index]]  = 1
        if flag:
            break
    for i in range(r):
        for j in range(c):
            if new_mtr[i][j] > 1:
                mtr[i][j] = 0
            else:
                mtr[i][j] = new_mtr[i][j]
    #         print(new_mtr[i][j], end = '')
    #     print()
    # print()
    if flag:
        break
if flag:
    print("kraj", cnt)
else:
    for i in range(r):
        for j in range(c):
            if mtr[i][j] == 0:
                print('.', end = '')
            elif mtr[i][j] == -1:
                print('I', end ='')
            else:
                print("R", end = '')
        print()