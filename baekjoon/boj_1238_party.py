INF = 987654321
def dijkstra(x, matrix):
    visited = [0]*(N+1)
    D = [INF]*(N+1)
    visited[x] = 1
    D[x] = 0
    for i in range(1, N+1):
        if matrix[x][i]: D[i] = matrix[x][i]
    for _ in range(N-1):
        mn = INF
        for i in range(1, N+1):
            if D[i] < mn and not visited[i]:
                mn, mn_idx = D[i], i
        visited[mn_idx] = 1
        for i in range(1, N+1):
            if matrix[mn_idx][i]: D[i] = min(D[i], D[mn_idx]+matrix[mn_idx][i])
    return D

N, M, X = map(int, input().split())
AM = [[0]*(N+1) for _ in range(N+1)]
BM = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    s, e, c = map(int, input().split())
    AM[s][e] = c
    BM[e][s] = c
go = dijkstra(X, AM)
back = dijkstra(X, BM)
result = max([go[i]+back[i] for i in range(1, N+1)])
print(result)