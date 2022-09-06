import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
n, w, l = map(int, input().split())
trucks = deque(list(map(int, input().split())))
bridge = deque()
cnt = 0
while True:
    if not trucks and not bridge:
        break
    bridge_copy = []
    weight_on_bridge = 0
    while bridge:
        weight, length = bridge.popleft()
        if length < w:
            weight_on_bridge += weight
            bridge_copy.append([weight, length+1])
    if trucks:
        if weight_on_bridge+ trucks[0] <= l:
            if len(bridge_copy) < w:
                bridge_copy.append([trucks.popleft(), 1])
    bridge = deque(bridge_copy)
    cnt +=1
    #print(bridge_copy)
print(cnt)