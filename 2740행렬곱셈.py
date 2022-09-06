import sys
input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
A = [list(map(int, input().split()))for _ in range(n)]
m, k = map(int, input().split())
B = [list(map(int, input().split()))for _ in range(m)]
answer = [[0 for _ in range(k)]for _ in range(n)]
for i in range(n):
    for j in range(k):
        for h in range(m):
            answer[i][j] += A[i][h] * B[h][j]
for i in range(n):
    for j in range(k):
        print(answer[i][j], end = ' ')
    print()
