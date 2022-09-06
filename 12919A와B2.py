import sys
input = lambda: sys.stdin.readline().rstrip()
S = input()
T = input()
flag = False
def transfer(t):
    if len(t) == len(S):
        return t == S
    if t[0] == 'B' and transfer(t[:0:-1]):
        return True
    if  t[-1] == 'A' and transfer(t[:-1]):
        return True
print(1 if transfer(T) else 0)