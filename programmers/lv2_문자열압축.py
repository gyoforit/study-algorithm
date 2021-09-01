def solution(string):
    answer = 987654321
    S = len(string)
    # 잘리는 구간의 길이
    for i in range(1, S+1):
        tmp = []
        for j in range(0, S, i):
            tmp.append(string[j:j+i])
        # total: 압축 후 길이
        # same: target과 같은 문자열의 개수
        # target: 현재 비교 대상
        total = 0
        same = 0
        target = tmp[0]
        for t in range(len(tmp)):
            if t == len(tmp)-1:
                if same:
                    total += (len(str(same+1))+len(target))
                else:
                    total += len(target)
                break
            if target == tmp[t+1]:
                same += 1
            else:
                if same:
                    total += (len(str(same+1))+len(target))
                else:
                    total += len(target)
                # 가지치기: 최솟값 초과했으면 더 이상 볼 필요 X
                if total >= answer:
                    break
                target = tmp[t+1]
                same = 0
        answer = min(answer, total)
    return answer