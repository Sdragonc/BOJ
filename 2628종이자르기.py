import sys
input = lambda: sys.stdin.readline().rstrip()
m, n = map(int, input().split())
line = int(input())
r, c = [0], [0]
for _ in range(line):
    l, num = map(int, input().split())
    if l == 0:
        r.append(num)
    else:
        c.append(num)
r.sort(); c.sort()
r.append(n);c.append(m)
r_max = 0
c_max = 0
for i in range(len(r)-1):
    if r_max < r[i+1] - r[i]:
        r_max = r[i+1] - r[i]
for i in range(len(c)-1):
    if c_max < c[i+1] - c[i]:
        c_max = c[i+1] - c[i]
print(c_max*r_max)