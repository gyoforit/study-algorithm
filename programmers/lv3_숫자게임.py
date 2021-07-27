def solution(A, B):
    A.sort()
    B.sort()
    answer = 0
    a, b = 0, 0
    while b <= len(B)-1:
        if A[a] < B[b]:
            answer += 1
            a += 1
            b += 1
        else:
            b += 1
    return answer