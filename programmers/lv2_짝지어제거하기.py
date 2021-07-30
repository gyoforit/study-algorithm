# 최대 길이 백만이므로 for문 한번에 해결해야 함
def solution(words):
    answer = -1
    stack = []
    for w in words:
        if stack:
            last = stack[-1]
            if last == w:
                stack.pop()
            else:
                stack.append(w)
        else:
            stack.append(w)

    answer = 1 if not stack else 0

    return answer