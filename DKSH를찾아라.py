import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
S = input()
DKSH = ["D", "K", "S", "H"]
answer = 0
new = ''
for i in range(n):
    if S[i] in DKSH:
        new += S[i]
visited = [False for _ in range(len(new))]
#print(new)
for i in range(len(new)):
    print(visited)
    if not visited[i]:
        if new[i]== 'D':
            if i != len(new)-1:
                count = [1, 0, 0, 0]
                current = 0
                idx = i+1
                visited[i] = True
                while idx < len(new):
                    if new[idx] == DKSH[current]:
                        count[current] += 1
                        #visited[idx] = True
                    else:
                        if current != 3:
                            if new[idx] == DKSH[current+1]:
                                current += 1
                                count[current] += 1
                                #visited[idx] = True
                    idx += 1
            total = 1
            print(count)
            flag = False
            for j in range(4):
                if count[j] == 0:
                    flag = True
                    break
                total *= count[j]
            if not flag:
                answer += total
print(answer)