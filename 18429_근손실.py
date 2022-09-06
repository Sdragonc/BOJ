import sys
from itertools import permutations
n, k = map(int, input().split())
kit = list(map(int, input().split()))
permu = list(permutations(kit, len(kit)))
cnt = 0
for pos in permu:
    three = 500
    flag = False
    for p in pos:
        three += p - k
        if three < 500:
            flag = True
            break
    if not flag:
        cnt += 1
print(cnt)