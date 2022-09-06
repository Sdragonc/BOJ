import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
five = n // 5
two = n // 2
for i in range(five, -1, -1):
    if (n - (i*5)) % 2 == 0:
        print(i+((n - (i*5)) // 2))
        exit()
print(-1)