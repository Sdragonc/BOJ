import sys
input = lambda: sys.stdin.readline().rstrip()
v, e = map(int, input().split())
edges = []
for _ in range(e):
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
parent = [i for i in range(v+1)]
res = 0
for cost, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        res += cost
print(cost)