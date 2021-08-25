INF = 987654321
def djikstra(start, matrix, N):
    D = [INF]*(N+1)
    visited = [0]*(N+1)
    D[start] = 0
    visited[start] = 1
    for i in range(1, N+1):
        if matrix[start][i]:
            D[i] = matrix[start][i]
    for _ in range(N-1):
        mn = INF
        for i in range(1, N+1):
            if D[i] < mn and not visited[i]:
                mn, mn_idx = D[i], i
        visited[mn_idx] = 1
        for i in range(1, N+1):
            if matrix[mn_idx][i]:
                D[i] = min(D[i], D[mn_idx]+matrix[mn_idx][i])
    return D

def solution(N, road, K):
    AM = [[0]*(N+1) for _ in range(N+1)]
    for a, b, c in road:
        if AM[a][b] or AM[b][a]:
            if c >= max(AM[a][b], AM[b][a]):
                continue
        AM[a][b] = c
        AM[b][a] = c
    D = djikstra(1, AM, N)
    answer = sum([1 for i in D if i<=K])

    return answer