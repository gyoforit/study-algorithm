import sys
from collections import deque

def DFS(x):
    if not dfs_check[x]:
        dfs_check[x] = 1
        dfs_ans.append(x)
        for i in AL[x]:
            DFS(i)

def BFS(x):
    checked = [0]*(N+1)
    queue = deque()
    route = [x]
    checked[x] = 1
    queue.append(x)
    while queue:
        target = queue.popleft()
        for t in AL[target]:
            if not checked[t]:
                checked[t] = 1
                route.append(t)
                queue.append(t)
    return route

N, M, V = map(int, input().split())
AL = [list() for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    AL[s].append(e)
    AL[e].append(s)
for i in range(N+1):
    AL[i].sort()
dfs_ans = []
dfs_check = [0]*(N+1)
DFS(V)
print(*dfs_ans)
print(*BFS(V))