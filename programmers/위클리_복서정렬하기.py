def solution(weights, head2head):
    answer = []
    L = len(weights)
    for i in range(L):
        records = head2head[i]
        weight = weights[i]
        total_fights = records.count('W') + records.count('L')
        winrate = 0 if not total_fights else records.count('W') / total_fights
        wincnt = 0
        for j in range(L):
            if weights[j] > weight and records[j] == 'W':
                wincnt += 1
        answer.append((winrate, wincnt, weight, i + 1))
    answer.sort(key=lambda x: (-x[0], -x[1], -x[2], x[3]))

    return [a[3] for a in answer]