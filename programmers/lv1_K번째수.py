def solution(array, commands):
    answer = []
    for start, end, idx in commands:
        tmp = sorted(array[start-1:end])[idx-1]
        answer.append(tmp)
    return answer