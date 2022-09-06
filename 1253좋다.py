import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
cnt = 0
for i in range(n):
    start, end = 0, n-1
    while True:
        if start == i:
            start += 1
        if end == i:
            end -= 1
        if start >= end:
            break
        if numbers[start] + numbers[end] > numbers[i]:
            end -= 1
        elif numbers[start] + numbers[end] < numbers[i]:
            start +=  1
        else:
            cnt += 1
            break
print(cnt)