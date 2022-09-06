n = int(input())
visited = [False for _ in range(n+1)]
for i in range(2, n):
    if not visited[i]:
        j = 2
        while i*j <= n:
            visited[i*j] = True
            j+= 1
prime = []
for i in range(2, n+1):
    if not visited[i]:
        prime.append(i)
start = 1
end = 1
cumulative = [0]
total = 0
ans = 0
for i in range(len(prime)):
    total += prime[i]
    cumulative.append(total)
while end <= len(prime):
    tempt = cumulative[end]-cumulative[start-1]
    if tempt == n:
        ans += 1
    if tempt >= n:
        start += 1
    else:
        end += 1
print(ans)