# 문자열일치 문제는 가장 끝 문자에 집중!
# 문자열이 일치한다 = 끝까지 일치한다 이기 때문에
# 리스트 슬라이싱해서 삭제하는 방법: del 사용
import sys
sys.stdin = open('input.txt')
target = input().rstrip()
boom = list(input().rstrip())
end = boom[-1]
B = len(boom)
stack = []
for t in target:
    stack.append(t)
    if t == end:
        if stack[-B:] == boom:
            del stack[-B:]

print(''.join(stack) if stack else 'FRULA')