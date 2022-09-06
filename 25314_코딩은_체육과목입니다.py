import sys
input = lambda: sys.stdin.readline().rstrip()
N = int(input())
ans = 'int'
for _ in range(N//4):
    ans = "long " + ans
print(ans)
