from copy import deepcopy
drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 핵심: DFS를 돌리고 난 후 원래 값으로 되돌리기(다음 턴을 위해서)

# sr, sc = 현재 이동중인 마을의 확진자수 / r, c =
def DFS(sr, sc, r, c, cnt):
    global min_tmp
    # 병원이라면 최솟값 갱신
    if town[r][c] == -1:
        min_tmp = min(min_tmp, cnt)
        return

    for dr, dc in drc:
        nr, nc = r+dr, c+dc
        # 이동하려는 곳이 범위 내 + 아직 방문하지 않았다면
        if 0 <= nr < N and 0 <= nc < N and town[nr][nc] != 0 and visited[nr][nc] == 0:
            # 원래의 값 백업시켜놓음
            backup = town[nr][nc]
            # 이동하려는 곳이 병원이라면 추가로 더하지 않고 DFS 보냄
            if town[nr][nc] == -1:
                visited[nr][nc] = 1
                DFS(sr, sc, nr, nc, cnt)
                visited[nr][nc] = 0
            # 병원이 아니라면
            else:
                # 가려는 곳의 확진자가 더 적다면 그 차이만큼 추가감염자 수 누적해서 DFS
                if town[nr][nc] < town[sr][sc]:
                    tmp = town[sr][sc]-town[nr][nc]
                    town[nr][nc] = town[sr][sc]
                    visited[nr][nc] = 1
                    DFS(sr, sc, nr, nc, cnt+tmp)
                    town[nr][nc] = backup
                    visited[nr][nc] = 0
                # 가려는 곳의 확진자가 같거나 많다면 추가 감염자 없이 누적
                else:
                    visited[nr][nc] = 1
                    DFS(sr, sc, nr, nc, cnt)
                    visited[nr][nc] = 0

T = int(input())
for t in range(1, T+1):
    N = int(input())
    town = [list(map(int, input().split())) for _ in range(N)]
    min_patients = 0
    # min_tmp = 987654321
    visited = [[0]*N for _ in range(N)]
    for r in range(0, N):
        for c in range(0, N):
            if town[r][c] != -1:
                min_tmp = 987654321
                DFS(r, c, r, c, 0)
                min_patients += min_tmp
                # min_tmp = 987654321
                town[r][c] = 0

    print("#%d %s" % (t, min_patients))