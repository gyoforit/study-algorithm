# 나보다 작은 애 터트릴 수 있는 기회는 한 번, 나머지는 무조건 나보다 큰 애가 터짐
# 따라서 가장 작은 풍선/양 사이드 풍선은 무조건 살아남음
# 가장 작은 풍선의 왼쪽: 내 왼쪽에 나보다 작은 애가 있으면 안됨
# 가장 작은 풍선의 오른쪽: 내 오른쪽에 나보다 작은 애가 있으면 안됨

def solution(a):
    A = len(a)
    min_balloon = a.index(min(a))
    now_min, now_min_2 = a[0], a[A-1]
    answer = 1
    for i in range(min_balloon):
        if now_min >= a[i]:
            now_min = a[i]
            answer += 1
    for i in range(A-1, min_balloon, -1):
        if now_min_2 >= a[i]:
            now_min_2 = a[i]
            answer += 1
    return answer