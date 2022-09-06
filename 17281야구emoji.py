import sys
from itertools import permutations
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
max_score = 0
innings = [list(map(int, input().split()))for _ in range(n)]
permu = permutations([i for i in range(1, 9)], 8)
for per in permu:
    per = list(per)
    per_deq = per[:3] + [0] + per[3:]
    points = 0
    idx = -1
    for inning in innings:
        out_count = 3
        b1, b2, b3 = 0, 0, 0
        while out_count > 0:
            idx = (idx+1) % 9
            if inning[per_deq[idx]] == 0:
                out_count -= 1
            elif inning[per_deq[idx]] == 1:
                points += b3
                b1, b2, b3 = 1, b1, b2
            elif inning[per_deq[idx]] == 2:
                points += b2+b3
                b1, b2, b3 = 0, 1, b1
            elif inning[per_deq[idx]] == 3:
                points += b1+b2+b3
                b1, b2, b3 = 0, 0, 1
            else:
                points += b1+b2+b3+1
                b1, b2, b3 = 0, 0, 0
    if max_score < points:
        max_score = points
print(max_score)