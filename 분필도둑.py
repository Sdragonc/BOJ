from re import A
import sys
from itertools import combinations
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
chalk = list(map(int, input().split()))
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
parent = [i for i in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    union_parent(parent, u, v)
group = [[]for _ in range(n+1)]
for i in range(len(parent)):
    group[parent[i]].append(i)
max_chalk = 0
print(parent)
for i in range(1, n+1):
    if group[i]:
        for j in range(1, len(group[i])+1):
            combi = list(combinations(group[i], j))
            print(combi)
            for c in combi:
                tempt_chalk = min(c)*j
                if max_chalk < tempt_chalk:
                    max_chalk = tempt_chalk
print(max_chalk)