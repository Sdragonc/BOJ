import sys
input = lambda: sys.stdin.readline().rstrip()
n, s = map(int, input().split())
permut = list(map(int, input().split()))
min_len = 1e9
cumulative = [0]
total = 0
for i in range(len(permut)):
    total += permut[i]
    cumulative.append(total)
start, end = 0, 0
while start < n+1 and end < n+1:
    if cumulative[end] - cumulative[start] < s:
        if start == 0 and end == n:
            print(0)
            exit()
        end += 1
    else:
        if min_len > end - start:
            min_len = end - start
        start += 1
print(min_len)