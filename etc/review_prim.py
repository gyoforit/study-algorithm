INF = 10**20
# 가장 거리 짧은 인접 노드 구하는 함수
def get_mincost(D, check):
    mn, mn_idx = INF, INF
    for i in range(N):
        if not check[i] and mn > D[i]:
            mn = D[i]
            mn_idx = i
    return mn_idx

# N개의 노드. x에서 출발하는 MST 구하는 함수
def prim(x, N):
    check = [0]*N
    D = [INF]*N
    D[x] = 0
    for _ in range(N):
        # x에서 가장 가깝고 방문 안한 노드 선정
        i = get_mincost(D, check)
        # 방문 체크
        check[i] = 1
        # i와 인접한 노드 중 방문하지 않은 노드들에 대해 거리 갱신
        for e, w in AL[i]:
            if not check[e]:
                D[e] = min(D[e], w)
    return D