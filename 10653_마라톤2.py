import sys
input = lambda: sys.stdin.readline().rstrip()
def dfs(x, y, cnt):
    global count
    #print(road)
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        #print(nx, ny)
        if nx < 0 or ny < 0 or nx >= R or ny >= C:
            continue
        #print(0)
        if visited[nx][ny]:
            continue
        #print(1)
        if road[nx][ny] == 'T':
            continue
        #print(2)
        if nx == 0 and ny == C-1:
            if cnt+1 == K:
                count += 1
            continue
        #print(3)
        dfs(nx, ny, cnt+1)
    visited[x][y] = False
R, C, K = map(int, input().split())
road = [input()for _ in range(R)]
visited = [[False for _ in range(C)]for _ in range(R)]
count = 0
dx = [1, -1, 0,  0]
dy = [0, 0, 1, -1]
dfs(R-1, 0, 1)
print(count)