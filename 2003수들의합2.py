import sys
input = lambda: sys.stdin.readline()
n, m = map(int, input().split())
arr = list(map(int, input().split()))
start, end = 1,1
cumul = [0]
total = 0
ans = 0
for i in range(n):
    total += arr[i]
    cumul.append(total)
#print(cumul)
while end <= n:
    total = cumul[end]-cumul[start-1]
    if total == m:
        ans += 1
    if total < m:
        end += 1
    else:
        start += 1
print(ans)