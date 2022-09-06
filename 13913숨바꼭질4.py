from collections import deque
import copy
n, k = map(int, input().split())
visited = [0 for _ in range(100001)]
q = deque()
q.append([n, [n]])
visited[n] = 0
if n == k:
    print(0)
    print(n)
elif n > k:
    print(n-k)
    for i in range(n, k-1, -1):
        print(i, end = ' ')
else:
    while q:
        x, route = q.popleft()
        pos = [x-1, x+1, 2*x]
        for p in pos:
            if 0 <= p <= 100000 and visited[p]==0:
                if  p == k:
                    print(visited[x]+1)
                    print(*route, end = ' ')
                    print(p)
                    exit()
                else:
                    visited[p] = visited[x]+1
                    q.append([p, route+[p]])
