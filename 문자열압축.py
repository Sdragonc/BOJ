import sys
input = lambda: sys.stdin.readline().rstrip()
def solution(s):
    answer = 1e9
    for i in range(1, len(s)//2+1):
        compare = s[:i]
        sentence = ""
        repeat = 1
        for j in range(1, len(s)//i):
            if compare != s[j*i:j*i+i]:
                if repeat != 1:
                    sentence += str(repeat)
                    repeat = 1
                    sentence += compare
                    compare = s[j*i:j*i+i]
                else:
                    sentence += compare
                    compare = s[j*i:j*i+i]
                if j == len(s)//i-1:
                    sentence += compare
            else:
                repeat += 1
                if j == len(s)//i-1:
                    sentence += str(repeat)
                    sentence += compare
        if len(s) % i != 0:
            sentence += s[-(len(s)%i):]
        if answer > len(sentence):
            answer = len(sentence)
    return answer
print(solution("a"))