import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
indegree = [0] * (n+1)
q = deque()
graph = [[]for _ in range(n+1)]
res = 0
time = [0 for _ in range(n+1)]
for i in range(1, n+1):
    t, *first = map(int, input().split())
    first = first[:-1]
    indegree[i] += len(first)
    time[i] = t
    if indegree[i]  == 0:
        q.append(i)
    else:
        for f in first:
            graph[f].append(i)
cost =  [0]*(n+1)
while q:
    x = q.popleft()
    for v in graph[x]:
        indegree[v] -= 1
        cost[v] = max(cost[v], time[x])
        if indegree[v] == 0:
            q.append(v)
            time[v] += cost[v]    
for i in range(1, n+1):
    print(time[i])
    
