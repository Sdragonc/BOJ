import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**9)
n = int(input())
graph = [[]for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
distance = [-1]*(n+1)
def dfs(x, cnt):
    for i in graph[x]:
        if distance[i[0]] == -1:
            distance[i[0]] = cnt+i[1]
            dfs(i[0], i[1]+cnt)
distance[1] = 0
dfs(1, 0)
start = distance.index(max(distance))
distance = [-1]*(n+1)
distance[start] = 0
dfs(start, 0)
print(max(distance))