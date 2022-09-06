import sys
input= lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 0, max(trees)
max_h = 0
while start <= end:
    mid = (start+end)//2
    total = 0
    for t in trees:
        if t > mid:
            total += t - mid
    if total >= m:
        max_h = mid
        start = mid + 1
    else:
        end = mid-1
print(max_h)