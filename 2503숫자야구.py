import sys
from itertools import permutations
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
question = []
for _ in range(n):
    num, strike, ball = input().split()
    strike, ball = int(strike), int(ball)
    question.append([num, strike, ball])
numbers = [str(i) for i in range(1, 10)]
pos = list(permutations(numbers, 3))
ans = []
pos = list(map(''.join, pos))
#print(pos)
for p in pos:
    flag = False
    for q in question:
        strike, ball = 0, 0
        for i in range(3):
            if p[i] in q[0]:
                if p[i] == q[0][i]:
                    strike += 1
                else:
                    ball += 1
        if strike != q[1] or ball != q[2]:
            flag = True
            break
    if not flag:
        ans.append(p)
print(len(ans))