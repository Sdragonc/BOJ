import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
switch = list(map(int, input().split()))
std_n = int(input())
students = []
for i in range(std_n):
    students.append(list(map(int, input().split())))
    students[i][1] -= 1
def switchch(n):
    if n == 0:
        return 1
    else:
        return 0
for std in students:
    if std[0] == 1:
        for i in range(std[1], n, std[1]+1):
            switch[i] = switchch(switch[i])
    else:
        j = 1
        switch[std[1]] = switchch(switch[std[1]])
        while True:
            if std[1] - j < 0 or std[1]+j > n-1:
                break
            if switch[std[1]-j] == switch[std[1]+j]:
                switch[std[1]-j] = switchch(switch[std[1]-j])
                switch[std[1]+j] = switchch(switch[std[1]+j])
            else:
                break
            j += 1
    #print(switch)
for i in range(len(switch)):
    if i % 20 == 0 and i != 0:
        print()
        print(switch[i], end = ' ')
    else:
        print(switch[i], end = ' ')