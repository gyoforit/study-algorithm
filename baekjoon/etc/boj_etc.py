# 백준 기타문제
# 210220
# 2167. 2차원 배열의 합
# python3으로 돌리면 시간초과, pypy3으로 돌려야 통과
# 나중에 동적계획법 배워서 다시 풀어보기
N, M = map(int, input().split())
arr = []
for n in range(N):
    arr.append(list(map(int, input().split())))
K = int(input())
for k in range(K):
    r1, c1, r2, c2 = map(int, input().split())
    result = 0
    for r in range(r1-1, r2):
        for c in range(c1-1, c2):
            result += arr[r][c]
    print(result)