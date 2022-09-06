import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
A, B, C = map(int, input().split())
ans = [False for _ in range(C+1)]
q = deque()
q.append([0, 0, C])
visited = []
while q:
    a, b, c = q.popleft()
    #print(a, b, c)
    if [a, b, c] not in visited:
        visited.append([a, b, c])
        if a == 0:
            ans[c] = True
    else:
        continue
    if a != 0:
        if b < B:
            if B-b > a:
                q.append([0, b+a, c])
            else:
                q.append([a-(B-b), B, c])
        if c < C:
            if C-c > a:
                q.append([0, b, c+a])
            else:
                q.append([a-(C-c), b, C])
    if b != 0:
        if a < A:
            if A-a > b:
                q.append([a+b, 0, c])
            else:
                q.append([A, b-(A-a), c])
        if c < C:
            if C-c > b:
                q.append([a, 0, c+b])
            else:
                q.append([a, b-(C-c), C])
    if c != 0:
        if a < A:
            if A-a > c:
                q.append([a+c, b, 0])
            else:
                q.append([A, b, c-(A-a)])
        if b < B:
            if B-b > c:
                q.append([a, b+c, 0])
            else:
                q.append([a, B, c-(B-b)])

for i in range(C+1):
    if ans[i]:
        print(i, end = ' ')