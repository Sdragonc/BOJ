import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
houses = list(map(int, input().split()))
houses.sort()
if len(houses) % 2 == 0:
    v1 = 0
    for i in range(n):
        v1 += houses[i]-houses[n//2-1]
    v2 = 0
    for i in range(n):
        v2 += houses[i]-houses[n//2]
    if v1 >= v2:
        print(houses[n//2-1])
    else:
        print(houses[n//2])
else:
    print(houses[n//2])