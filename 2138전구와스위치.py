import sys
import copy
input= lambda: sys.stdin.readline().rstrip()
n = int(input())
start = list(input())
end = list(input())
s1 = copy.deepcopy(start)
s2 = copy.deepcopy(start)
def flip(s):
    if s == '0':
        return '1'
    else:
        return '0'
def firstclick(start):
    cnt = 1
    start[0] = flip(start[0])
    start[1] = flip(start[1])
    for i in range(1, n):
        if i == n-1:
            if start[i-1] != end[i-1]:
                start[i] = flip(start[i])
                start[i-1] = flip(start[i-1])
                cnt += 1
        else:
            if start[i-1] != end[i-1]:
                start[i] = flip(start[i])
                start[i-1] = flip(start[i-1])
                start[i+1] = flip(start[i+1])
                cnt += 1
    if start == end:
        return cnt
    else:
        return -1
def firstNoClick(start):
    cnt = 0
    for i in range(1, n):
        if i == n-1:
            if start[i-1] != end[i-1]:
                start[i] = flip(start[i])
                start[i-1] = flip(start[i-1])
                cnt += 1
        else:
            if start[i-1] != end[i-1]:
                start[i] = flip(start[i])
                start[i-1] = flip(start[i-1])
                start[i+1] = flip(start[i+1])
                cnt += 1
    if start == end:
        return cnt
    else:
        return -1
res1 = firstclick(s1)
res2 = firstNoClick(s2)
if(res1>=0 and res2>=0):
    print(min(res1,res2))
elif(res1>=0 and res2<0):
    print(res1)
elif(res1<0 and res2>=0):
    print(res2)
else:
    print(-1)