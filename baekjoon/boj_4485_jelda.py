from collections import deque
drc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def BFS(r, c):
    D = [[987654321]*N for _ in range(N)]
    D[r][c] = cave[r][c]
    queue = deque()
    queue.append((r, c))
    while queue:
        tr, tc = queue.popleft()
        for dr, dc in drc:
            nr, nc = tr+dr, tc+dc
            if 0 <= nr < N and 0 <= nc < N:
                if D[nr][nc] > D[tr][tc]+cave[nr][nc]:
                    D[nr][nc] = D[tr][tc]+cave[nr][nc]
                    queue.append((nr, nc))
    return D[-1][-1]
idx = 1
while True:
    N = int(input())
    if N == 0:
        break
    cave = [list(map(int, input().split())) for _ in range(N)]
    print("Problem %d: %d" % (idx, BFS(0, 0)))
    idx += 1