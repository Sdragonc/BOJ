n, k = map(int, input().split())
visited = [False for _ in range(n+1)]
cnt = 0
for i in range(2, n+1):
    j = 1
    while i * j <= n:
        if not visited[i*j]:
            visited[i*j] = True
            cnt += 1
        if cnt == k:
            break
        j += 1
    if cnt == k:
        print(i*j)
        break