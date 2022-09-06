import sys
input = lambda: sys.stdin.readline().rstrip()
m, n = map(int, input().split())
cate = [1 for _ in range(2*m-1)]
for _ in range(n):
    zero, one, two = map(int, input().split())
    for i in range(zero, zero+one):
        cate[i] += 1
    for i in range(zero+one, len(cate)):
        cate[i] += 2
for i in range(m):
    for j in range(m):
        if j == 0:
            print(cate[m-1-i], end = ' ')
        else:
            print(cate[m-1+j], end = ' ')
    print()