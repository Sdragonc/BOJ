import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
distance = [1e9 for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
route = [[] for _ in range(n+1)]
start, end = map(int, input().split())
distance[start] = 0
q = []
heapq.heappush(q, [0, start, [start]])
while q:
    dist, now, r = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for v in graph[now]:
        tempt_r = [r[i] for i in range(len(r))]
        cost = dist + v[1]
        if cost < distance[v[0]]:
            distance[v[0]] = cost
            tempt_r.append(v[0])
            route[v[0]] = tempt_r
            heapq.heappush(q, [cost, v[0], tempt_r])
print(distance[end])
print(len(route[end]))
print(*route[end])