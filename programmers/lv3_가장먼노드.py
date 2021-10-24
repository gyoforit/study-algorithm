# 가중치 없는 그래프라 다익스트라 아닌 bfs로 최단거리 측정
from collections import deque
INF = 10**20
def solution(n, edge):
    visited = [0]*n
    D = [INF]*n
    AL = [[] for _ in range(n)]
    for ed in edge:
        AL[ed[0]-1].append(ed[1]-1)
        AL[ed[1]-1].append(ed[0]-1)
    queue = deque()
    queue.append((0, 0))
    visited[0] = 1
    D[0] = 0
    while queue:
        point, distance = queue.popleft()
        for adj in AL[point]:
            if not visited[adj]:
                visited[adj] = 1
                D[adj] = min(D[adj], distance+1)
                queue.append((adj, distance+1))
    answer = D.count(max(D))
    return answer