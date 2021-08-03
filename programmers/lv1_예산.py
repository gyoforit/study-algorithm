def solution(d, budget):
    d.sort()
    for (i, dept) in enumerate(d):
        if budget < dept:
            answer = i
            break
        budget -= dept
    else:
        answer = len(d)
    return answer