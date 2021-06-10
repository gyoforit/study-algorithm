drc = [(0, 2), (2, 0), (0, -2), (-2, 0)]
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    grid = [[0]*N for _ in range(M)]
    cnt = 0
    for r in range(M):
        for c in range(N):
            if not grid[r][c]:
                cnt += 1
                for dr, dc in drc:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<M and 0<=nc<N:
                        grid[nr][nc] = 1

    print("#%d %d" % (t, cnt))