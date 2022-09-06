import sys
input = lambda: sys.stdin.readline().rstrip()
n, m, a, k = map(int, input().split())
max_rank = 0
min_rank = 0
if m == 1:
    print(a-k+1, a-k+1)
else:
    if a-k >= n-1:
        max_rank =  n
    else:
        max_rank = a-k+1
    min_rank = (a-k)//m + 2
    print(max_rank, min_rank)