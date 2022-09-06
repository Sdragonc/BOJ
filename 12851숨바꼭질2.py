import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
n, k = map(int, input().split())
visited = [[-1, 0]for _ in range(100001)]
if n == k:
    print(0)
    print(1)
elif n > k:
    print(n-k)
    print(1)
else:
    q = deque()
    q.append(n)
    visited[n] = [0, 1]
    while q:
        x= q.popleft()
        pos = [x+1, x-1, 2*x]
        # if cnt > ans[0]:
        #     continue
        for p in pos:
            if 0 <= p <= 100000:
                if visited[p][0] == -1:
                    visited[p][0] = visited[x][0] +1
                    visited[p][1] = visited[x][1]
                    q.append(p)
                elif visited[p][0] == visited[x][0]+1:
                    visited[p][1] += visited[x][1]
    print(*visited[k], sep='\n')