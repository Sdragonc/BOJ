import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
numbers = list(map(int, input().split()))
numbers = list(map(str, numbers))
numbers.sort(key = lambda x: x*10, reverse = True)
print(str(int(''.join(numbers))))