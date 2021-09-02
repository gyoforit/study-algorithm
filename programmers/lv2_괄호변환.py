upside_down = {'(': ')', ')': '('}

# 올바른 괄호인지 체크
def is_right(brackets):
    stack = []
    for bracket in brackets:
        if not stack or bracket == '(':
            stack.append(bracket)
        elif bracket == ')':
            if stack and stack[-1] == '(':
                stack.pop()
    if stack:
        return False
    return True

def solution(brackets):
    if not brackets or is_right(brackets):
        return brackets
    a, b = 0, 0
    idx = 0
    for i in range(len(brackets)):
        if brackets[i] == '(':
            a += 1
        elif brackets[i] == ')':
            b += 1
        if a and b and a == b:
            idx = i
            break

    u, v = brackets[:idx+1], brackets[idx+1:]

    if is_right(u):
        return u+solution(v)
    new_u = ''
    for n in u[1:-1]:
        new_u += upside_down[n]
    return '(' + solution(v) + ')' + new_u