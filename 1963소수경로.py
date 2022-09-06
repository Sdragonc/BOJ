import sys
from collections import deque
import copy
input = lambda: sys.stdin.readline().rstrip()
def prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
t = int(input())
for _ in range(t):
    start, end = map(list, input().split())
    q = deque()
    q.append([start, 0])
    flag = False
    visited = [False for _ in range(10000)]
    while q:
        num, cnt = q.popleft()
        if num == end:
            print(cnt)
            flag = True
            break
        for i in range(4):
            for j in range(10):
                if i == 0 and j == 0:
                    continue
                if int(num[i]) == j:
                    continue
                t_num = copy.deepcopy(num)
                t_num[i] = str(j)
                if not visited[int(''.join(t_num))]:
                    if prime(int(''.join(t_num))):
                        q.append([t_num, cnt+1])
                        visited[int(''.join(t_num))] = True
    if not flag:
        print("Impossible")