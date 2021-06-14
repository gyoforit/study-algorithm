def solution(A, K):
    # A의 범위가 0 이상이므로 빈 배열일 때는 따로 조건 분기 항상 경계값에 주의!
    if not A:
        result = []
    else:
        start_idx = len(A) - (K % len(A))
        result = A[start_idx:]+ A[:start_idx]
    return result