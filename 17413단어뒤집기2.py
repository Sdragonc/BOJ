import sys
input = lambda: sys.stdin.readline().rstrip()
s = input()
answer = ''
stack = []
bracket = False
for i in range(len(s)):
    if s[i]  == '<':
        bracket = True
        while stack:
            answer += stack.pop()
        answer += s[i]
    elif s[i] == '>':
        bracket = False
        answer += s[i]
    elif bracket:
        answer += s[i]
    elif s[i] == ' ':
        while stack:    
            answer += stack.pop()
        answer += s[i]
    else:
        stack.append(s[i])
if stack:
    while stack:
        answer += stack.pop()
print(answer)