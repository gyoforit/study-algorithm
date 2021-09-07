def solution(citations):
    mx = max(citations)
    cnt_array = [0]*(mx+1)
    for citation in citations:
        cnt_array[citation] += 1
    for i in range(mx, -1, -1):
        if sum(cnt_array[i:]) >= i and sum(cnt_array[:i]) <= i:
            return i
    return 0