import sys
from collections import deque
from itertools import permutations
input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
ans = []
def bfs(q, result):
    global ans
    x = q.popleft()
    print(q, result)
    result.append(x)
    tempt = []
    for v in graph[x]:
        indegree[v] -= 1
        if indegree[v] == 0:
            tempt.append(v)
    per = list(permutations(tempt, len(tempt)))
    print(per)
    if not q and not per:
        print(result)
        ans.append(result)
        return
    for p in per:
        tempt_q = deque(q[i] for i in range(len(q)))
        for j in p:
            tempt_q.append(j)
        bfs(tempt_q, result)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
tem = []
for i in range(1, n+1):
    if indegree[i] == 0:
        tem.append(i)
per_t = list(permutations(tem, len(tem)))
for pt in per_t:
    q = deque()
    for p in pt:
        q.append(p)
    bfs(q, [])
print(ans)