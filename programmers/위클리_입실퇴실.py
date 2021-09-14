def solution(enter, leave):
    answer = [[] for _ in range(len(enter)+1)]
    room = []
    s, e = 0, 0
    while s < len(enter) or e < len(leave):
        if leave[e] not in room:
            answer[enter[s]] = room[:]
            room.append(enter[s])
            s += 1
        else:
            room.remove(leave[e])
            e += 1
    for idx, ans in enumerate(answer):
        for p in ans:
            answer[p].append(idx)
    return [len(set(ans)) for ans in answer][1:]