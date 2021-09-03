import math
def solution(progresses, speeds):
    days = [math.ceil((100-progresses[i])/speeds[i]) for i in range(len(progresses))]
    answer = []
    target = days[0]
    cnt = 1
    for i in range(1, len(days)):
        if target >= days[i]:
            cnt += 1
        else:
            target = days[i]
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)
    return answer