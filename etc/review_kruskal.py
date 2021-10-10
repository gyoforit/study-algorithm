# 자신의 부모 노드 찾는 함수
def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

# y의 부모를 x의 부모로
def union(x, y):
    p[find_set(y)] = find_set(x)

def kruskal(arr):
    cnt = 0
    for s, e, w in arr:
        # 싸이클 형성이 안 되면, 즉 부모가 다르면
        if find_set(s) != find_set(e):
            cnt += w
            union(s, e)
    return cnt

V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
# 거리순으로 오름차순 정렬
edges = sorted(edges, key=lambda x: x[2])
p = list(range(V+1))
kruskal(edges)