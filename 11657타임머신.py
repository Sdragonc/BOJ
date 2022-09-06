import sys
input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
visited = [False for _ in range(n+1)]
distance = [1e9 for _ in range(n+1)]
distance[1] = 0
edges = []
for _ in range(m):
    edges.append(list(map(int, input().split())))
def bfs(start):
    for i in range(n):
        for j in range(m):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            if distance[cur] != 1e9 and distance[next_node]>distance[cur]+cost:
                distance[next_node] = distance[cur]+cost
                if i == n-1:
                    return True
    return False
negative= bfs(1)
if negative:
    print(-1)
else:
    for i in range(2, n+1):
        if distance[i]==1e9:
            print(-1)
        else:
            print(distance[i])
