bonus = {'S': 1, 'D': 2, 'T': 3}

def solution(dartResult):
    dartResult = dartResult.replace('10', 'a')
    points = []
    for d in dartResult:
        if d.isdigit() or d == 'a':
            num = 10 if d == 'a' else int(d)
            points.append(num)
        elif d in {'S', 'D', 'T'}:
            points[-1] **= bonus[d]
        elif d == '*':
            points[-1] *= 2
            if len(points) >= 2:
                points[-2] *= 2
        elif d == '#':
            points[-1] = -1 * (points[-1])
    answer = sum(points)
    return answer