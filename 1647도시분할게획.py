import sys
input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append([cost, a, b])
edges.sort()
def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
res = []
parent = [i for i in range(n+1)]
for cost,a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        res.append(cost)
print(sum(res)-max(res))