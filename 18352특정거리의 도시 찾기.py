import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()
n, m, k, x = map(int, input().split()) 
distance = [1e9 for _ in range(n+1)]
distance[x] = 0
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
q = []
heapq.heappush(q, (0, x))
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + 1
        if cost < distance[i]:
            distance[i] = cost
            heapq.heappush(q, (cost, i))
ans = []
for i in range(1, n+1):
    if distance[i] == k:
        ans.append(i)
if not ans:
    print(-1)
else:
    print(*ans, sep = '\n')
    
