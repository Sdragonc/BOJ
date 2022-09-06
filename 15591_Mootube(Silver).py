import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
n, Q = map(int, input().split())
mootube = [[] for _ in range(n+1)]
for _ in range(n-1):
    p, q, r = map(int, input().split())
    mootube[p].append([q, r])
    mootube[q].append([p, r])
for _ in range(Q):
    k, v = map(int, input().split())
    visited = [0] * (n+1)
    ans = 0
    q = deque()
    q.append([v, 1e9])
    while q:
        x, usado = q.popleft()
        visited[x] = True
        for h in mootube[x]:
            if visited[h[0]]:
                continue
            if min(usado, h[1]) >= k:
                ans += 1
            if usado > h[1]: 
                q.append([h[0], h[1]])
            else:
                q.append([h[0], usado])
    print(ans)