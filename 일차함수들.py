import sys
input=  lambda: sys.stdin.readline().rstrip()
n = int(input())
W = []
for _ in range(n):
    W.append(list(map(int, input().split())))
W.sort()
answer = 0
for i in range(n, 0, -1):
    answer += W[i-1][0]*i + W[i-1][1]
print(answer)