import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
jump = list(map(int, input().split()))
q = deque()
q.append([0, 0])
visited = [False for _ in range(n)]
if n == 1:
    print(0)
    exit()
while q:
    x, cnt = q.popleft()
    if jump[x] != 0:
        for i in range(jump[x], 0, -1):
            if x + i == n-1:
                print(cnt+1)
                exit()
            if x+i >= n:
                continue
            if not visited[x+i]:
                q.append([x+i, cnt+1])
                visited[x+i] = True
print(-1)