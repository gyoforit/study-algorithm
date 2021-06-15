def solution(A):
    if not A:
        result = 1
    else:
        max_num = max(A)
        length = len(A)
        # 중간에 숫자가 빠져있는 경우
        if max_num != length:
            total = sum(list(range(1, max_num + 1)))
            result = total - sum(A)
        # 모든 수가 다 있는 경우 -> 최댓값+1 이 빠져있음
        else:
            result = max_num + 1

    return result