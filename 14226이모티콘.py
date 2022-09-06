import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
s = int(input())
visited = [[False for _ in range(1001)] for _ in range(1001)]
q = deque()
visited[1][0] = True
q.append([1, 0, 0])
while q:
    emoji, clipboard, cnt = q.popleft()
    if emoji == s:
        print(cnt)
        exit()
    pos = []
    if 0 <= emoji+clipboard <= 1000:
        if not visited[emoji+clipboard][clipboard]:
            if clipboard != 0:
                visited[emoji+clipboard][clipboard] = True
                q.append([emoji+clipboard, clipboard, cnt+1])
    q.append([emoji, emoji, cnt+1])
    if emoji >= 0:
        q.append([emoji-1, clipboard, cnt+1])