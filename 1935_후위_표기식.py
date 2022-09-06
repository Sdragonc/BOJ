import sys
input = lambda: sys.stdin.readline().rstrip()
operation = input()
op_stack = []
ans = ''
for o in operation:
    if 65 <= ord(o) <= 90:
        ans += o
    else:
        if o == "(":
            op_stack.append(o)
        elif o == '*' or o == '/':
            while op_stack  and (op_stack[-1] == '*' or op_stack[-1] == '/'):
                ans +=op_stack.pop()
            op_stack.append(o)
        elif o == '+' or o == '-':
            while op_stack and op_stack[-1] != '(':
                ans +=op_stack.pop()
            op_stack.append(o)
        elif o == ')':
            while op_stack and op_stack[-1] != '(':
                ans +=op_stack.pop()
            op_stack.pop()
while op_stack:
    ans +=op_stack.pop()
print(ans)