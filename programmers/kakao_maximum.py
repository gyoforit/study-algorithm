import itertools

def DFS(lv, expression, ops):
    if lv == len(ops)-1:
        return str(eval(expression))
    tmp = ops[lv]
    if tmp == '+':
        result = '+'.join(DFS(lv+1, e, ops) for e in expression.split(tmp))
    elif tmp == '-':
        result = '-'.join(DFS(lv+1, e, ops) for e in expression.split(tmp))
    elif tmp == '*':
        result = '*'.join(DFS(lv+1, e, ops) for e in expression.split(tmp))
    return str(eval(result))

def solution(expression):
    answer = 0
    ops = []
    for e in expression:
        if e in {'+', '-', '*'}:
            ops.append(e)
    pers = list(itertools.permutations(list(set(ops))))
    for p in pers:
        result = abs(int(DFS(0, expression, p)))
        answer = max(answer, result)
    return answer

# print(solution("100-200*300-500+20"))
# print(solution("50*6-3*2"))