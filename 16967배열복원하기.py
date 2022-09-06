import sys
input = lambda: sys.stdin.readline().rstrip()
h, w, x, y = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(h+x)]
A = [[0 for _ in range(w)]for _ in range(h)]
for i in range(x):
    for j in range(w):
        A[i][j] = B[i][j]
for i in range(h):
    for j in range(y):
        A[i][j] = B[i][j]
for i in range(x, h):
    for j in range(y,w):
        A[i][j] = B[i][j] - A[i-x][j-y]
for i in range(h):
    for j in range(w):
        print(A[i][j], end = ' ')
    print()