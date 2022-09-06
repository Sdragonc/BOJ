n = int(input())
ans = []
cnt = 0
for i in range(0, n+1):
    tempt = [n]
    tempt.append(n-i)
    while True:
        if tempt[-2] - tempt[-1] < 0:
            break
        tempt.append(tempt[-2] - tempt[-1])
    if cnt < len(tempt):
        ans = tempt
        cnt = len(tempt)
print(len(ans))
print(*ans)