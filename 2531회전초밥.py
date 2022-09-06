import sys
input = lambda: sys.stdin.readline().rstrip()
n, d, k, c = map(int, input().split())
sushi = []
for _ in range(n):
    sushi.append(int(input()))
start, end = 0, 0
hash = dict()
for i in range(1, d+1):
    hash[i] = 0
cnt = 0
max_cnt = 0
flag = False
while True:
    if flag and start % n == 0:
        break
    if end - start == k:
        start += 1
        flag = True
        if hash[sushi[start%n]] == 1:
            cnt -= 1
        hash[sushi[start%n]] -= 1
    end += 1
    if not hash[sushi[end%n]]:
            cnt += 1
            hash[sushi[end%n]] += 1
            if not hash[c]:
                if max_cnt < cnt+1:
                    max_cnt = cnt+1
            else:
                if max_cnt < cnt:
                    max_cnt = cnt
    else:
        hash[sushi[end%n]] += 1
print(max_cnt)