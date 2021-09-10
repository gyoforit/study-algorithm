def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt = [0, 0, 0, 0]
    l1, l2, l3 = len(p1), len(p2), len(p3)
    for i in range(len(answers)):
        if answers[i] == p1[i%l1]:
            cnt[1] += 1
        if answers[i] == p2[i%l2]:
            cnt[2] += 1
        if answers[i] == p3[i%l3]:
            cnt[3] += 1
    mx = max(cnt)
    answer = sorted([i for i, c in enumerate(cnt) if c == mx ])
    return answer