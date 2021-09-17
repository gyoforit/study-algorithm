def solution(scores):
    result = ''
    answer = []
    scores = list(zip(*scores))
    L = len(scores)
    for i in range(L):
        score = list(scores[i])
        target = score[i]
        flag = 0
        if max(score) == target or min(score) == target:
            if score.count(target) <= 1:
                score.remove(target)
                answer.append(sum(score)/len(score))
                flag = 1
        if not flag:
            answer.append(sum(score)/len(score))
    for ans in answer:
        if ans >= 90:
            result += 'A'
        elif ans >= 80:
            result += 'B'
        elif ans >= 70:
            result += 'C'
        elif ans >= 50:
            result += 'D'
        else:
            result += 'F'
    return result