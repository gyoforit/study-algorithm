# sys.stdin.readline은 공백문자도 받아와서 여기에는 적합하지 않음
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
bracket = {')': '(', '}': '{', ']': '['}
result = []
while True:
    sentence = input()
    if sentence == '.':
        break
    stack = []
    answer = ''
    for s in sentence:
        if s in {'(', '{', '['}:
            stack.append(s)
        elif s in bracket.keys():
            if stack and stack[-1] == bracket[s]:
                stack.pop(-1)
            else:
                answer = 'no'
                break
    if not answer:
        answer = 'no' if stack else 'yes'

    result.append(answer)

for r in result:
    print(r)