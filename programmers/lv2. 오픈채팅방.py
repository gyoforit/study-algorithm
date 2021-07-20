def solution(record):
    answer = []
    nickname = dict()
    timeline = []
    for r in record:
        tmp = r.split()
        if tmp[0] == 'Enter' or tmp[0] == 'Change':
            nickname[tmp[1]] = tmp[2]
        if tmp[0] == 'Enter' or tmp[0] == 'Leave':
            timeline.append((tmp[0], tmp[1]))

    for t in timeline:
        name = nickname.get(t[1])
        if t[0] == 'Enter':
            answer.append(name+'님이 들어왔습니다.')
        elif t[0] == 'Leave':
            answer.append(name+'님이 나갔습니다.')

    return answer