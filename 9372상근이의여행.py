import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
m = int(input())
graph = [[]for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
answer = 0
visited = [False for _ in range(n+1)]
visited[1] = True
#answer += len(graph[1])
for v in graph[1]:
    visited[v] = True
    answer += 1
for v in graph[1]:
    for x in graph[v]:
        if not visited[x]:
            answer += 1
            visited[x]= True
print(answer)