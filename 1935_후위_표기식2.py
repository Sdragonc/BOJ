import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
num_stack = []
expression = input()
dic = {}
for i  in range(65, 65+n):
    dic[chr(i)] = int(input())
for e in expression:
    if e.isalpha():
        num_stack.append(dic[e])
    else:
        x = num_stack.pop()
        y = num_stack.pop()
        exp = str(y)+e+str(x)
        num_stack.append(eval(exp))
print("{:.2f}".format(num_stack.pop()))