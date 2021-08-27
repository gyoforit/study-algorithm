def solution(participant, completion):
    name_dict = dict()
    for p in participant:
        if not name_dict.get(p):
            name_dict[p] = 1
        else:
            name_dict[p] += 1
    for c in completion:
        name_dict[c] += 1

    for name in name_dict.keys():
        if name_dict[name] % 2:
            answer = name
    return answer