# DFS는 시간초과 ㅠㅠ -> DP로 풀어보기!
def knapsack(start, now_v, now_c):
    global mx
    if now_c > mx:
        mx = now_c

    for i in range(start, N):
        if now_c + expected[i] <= mx: break
        if now_v + V[i] > K: continue
        knapsack(i+1, now_v+V[i], now_c+C[i])

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    V, C = [], []
    for _ in range(N):
        v, c = map(int, input().split())
        V.append(v)
        C.append(c)

    expected = [0] * N
    expected[N-1] = C[N-1]
    for i in range(N-2, -1, -1):
        expected[i] = expected[i+1]+C[i]

    mx = 0
    knapsack(0, 0, 0)
    print("#%d %d" % (t, mx))
