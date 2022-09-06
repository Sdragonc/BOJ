import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
time = [0]*(n+1)
graph= {}
for i in range(1, n+1):
    t, cnt, *first = map(int, input().split())
    time[i] = t
    #print(t, cnt, first)
    if cnt != 0:
        for j in first:
            if i in graph:
                graph[i].append(j)
            else:
                graph[i] = [j]
#print(graph)
for i in range(1, n+1):
    if i in graph:
        t = 0
        for j in graph[i]:
            t = max(t, time[j])
        #print(t)
        time[i] += t
print(max(time))
    