import sys
input= lambda: sys.stdin.readline().rstrip()
n = int(input())
rank = list()
for _ in range(n):
    rank.append(int(input()))
rank.sort()
complain = 0
for i in range(1, n+1):
    complain += abs(rank[i-1] - i)
print(complain)