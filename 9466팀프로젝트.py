import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(100001)
t = int(input())
def dfs(x):
    visited[x] = True
    global ans
    cycle.append(x)
    if visited[choice[x]]:
        if choice[x] in cycle:
            ans += cycle[cycle.index(choice[x]):]
        return
    else:
        dfs(choice[x])
for _ in range(t):
    n = int(input())
    visited = [False for _ in range(n+1)]
    choice = [0]
    choice += list(map(int, input().split()))
    ans = []
    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)
    print(n-len(ans))