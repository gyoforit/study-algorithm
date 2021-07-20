def solution(N, stages):
    cnt_array = [0]*(N+2)
    fail = []
    for stage in stages:
        cnt_array[stage] += 1
    for c in range(1, N+1):
        tmp = cnt_array[c]/sum(cnt_array[c:]) if sum(cnt_array[c:]) else 0
        fail.append((c, tmp))
    fail = sorted(fail, key=lambda x: (-x[1], x[0]))
    answer = [f[0] for f in fail]
    return answer