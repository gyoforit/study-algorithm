def dijkstra():
    # 방문 표시 체크하는 배열
    visited = [0]*(V+1)
    # 0에서 타 정점 간의 거리 담은 배열
    D = [987654321112345678] * (V+1)
    # 출발정점(0) 방문 체크 및 거리 0으로 설정
    visited[0] = 1
    D[0] = 0
    # 출발지에서 이어진 점들의 거리 갱신
    for e, w in AL[0]:
        D[e] = w
    # 출발지 제외한 V개의 정점까지의 거리 구하는 거니까 V번 반복
    for _ in range(V):
        mn = 98765432145678
        for i in range(V+1):
            # 정점 중 아직 방문하지 않았고, 출발지로부터 최소거리인 정점 찾기
            if D[i] < mn and not visited[i]:
                mn, mn_idx = D[i], i
        # 가장 가까운 거리의 정점 방문 체크
        visited[mn_idx] = 1
        # 해당 정점의 인접 정점 중 이 정점을 거쳐서 가는게 더 빠르다면 갱신
        for e, w in AL[mn_idx]:
            D[e] = min(D[e], D[mn_idx]+w)
    return D


# 0~V 정점, E개의 간선
V, E = map(int, input().split())
# 인접 리스트에 (도착지, 거리) append
AL = [[] for _ in range(V+1)]
for _ in range(E):
    s, e, w = map(int, input().split())
    AL[s].append((e, w))
    dijkstra()