import sys
input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
six = []
one = []
for _ in range(m):
    s, o = map(int, input().split())
    six.append(s)
    one.append(o)
six.sort()
one.sort()
#print(one)
print(min((n//6+1)*six[0], (n//6)*six[0]+(n%6)*one[0], n*one[0]))
