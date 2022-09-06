cards = ''.join(input().split())
min_num = 1e9
for i in range(4):
    num = ''
    num += cards[i]
    j = i
    for _ in range(3):
        j += 1
        if j == 4:
            j = 0
        num += cards[j]
    if min_num > int(num):
        min_num = int(num)
def deter(n):
    min_num = 1e9
    n = str(n)
    for i in range(4):
        num = ''
        num += n[i]
        j = i
        for _ in range(3):
            j += 1
            if j == 4:
                j = 0
            num += n[j]
        if min_num > int(num):
            min_num = int(num)
    return min_num
cnt = 0
for i in range(1111, min_num+1):
    flag = False
    for j in str(i):
        if j == '0':
            flag = True
            break
    if (deter(i) != i):
        flag = True
    if not flag:
        cnt += 1
print(cnt)

    