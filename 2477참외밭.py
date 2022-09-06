import sys
input = lambda: sys.stdin.readline().rstrip()
k = int(input())
max_w = 0
max_h = 0
minus_w = 0
minus_h = 0
visited = [False for _ in range(4)]
for _ in range(6):
    d, l = map(int, input().split())
    if d== 1 or d == 2:
        if d == 1:
            visited[0] = True
        else:
            visited[1] = True
        if max_w < l:
            max_w = l
        if d == 1 and visited[1]:
            minus_w = l
        elif d == 2 and visited[0]:
            minus_w = l
    else:
        if d == 3:
            visited[2] = True
        else:
            visited[3] = True
        if max_h < l:
            max_h = l
        if d == 3 and visited[3]:
            minus_h = l
        elif d == 4 and visited[2]:
            minus_h = l
print(max_w, max_h, minus_w, minus_h)
print(k*(max_w*max_h - minus_w*minus_h))