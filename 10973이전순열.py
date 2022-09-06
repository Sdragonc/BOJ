import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
permut = list(map(int, input().split()))
flag = False
for i in range(n-1, 0, -1):
    if permut[i] < permut[i-1]:
        flag = True
        for j in range(n-1, i-1, -1):
            if permut[j] < permut[j-1]:
                permut[i-1], permut[j]  = permut[j], permut[i-1]
                permut = permut[:i] + sorted(permut[i:], reverse = True)
                break
        break
if not flag:
    print(-1)
else:
    print(*permut, sep = ' ')