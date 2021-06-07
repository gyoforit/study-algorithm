# 핵심: DFS를 돌리고 난 후 원래 값으로 되돌리기(다음 턴을 위해서) + 리스트 복사
import copy
drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# sr, sc = 현재 이동중인 감염자들의 마을 좌표 / r, c = 이동 중인 마을 감염자들의 현재 위치
def DFS(sr, sc, r, c, cnt):
    global min_tmp, copy_town
    # 병원이라면 최솟값 갱신 + town의 상태를 copy_town에 복사 (최솟값 경신될 때마다 계속 바뀜)
    if town[r][c] == -1:
        if cnt < min_tmp:
            min_tmp = cnt
            copy_town = copy.deepcopy(town)
        return
    # 상하좌우로 이동하며
    for dr, dc in drc:
        nr, nc = r+dr, c+dc
        # 이동하려는 곳이 범위 내에 있고, 0이 아니고, 아직 방문하지 않았다면
        if 0 <= nr < N and 0 <= nc < N and town[nr][nc] != 0 and visited[nr][nc] == 0:
            # 원래의 값 미리 백업시켜놓음
            backup = town[nr][nc]
            # 이동하려는 곳이 병원이라면 추가감염자 수 더하지 않고 그대로 DFS 보냄
            if town[nr][nc] == -1:
                visited[nr][nc] = 1
                DFS(sr, sc, nr, nc, cnt)
                visited[nr][nc] = 0
            # 병원이 아니라면
            else:
                # 가려는 곳의 확진자가 더 적다면, 추가감염자 수 반영 하고 방문 체크 후, 추가감염자 수 누적해서 DFS
                if town[nr][nc] < town[sr][sc]:
                    tmp = town[sr][sc]-town[nr][nc]
                    town[nr][nc] = town[sr][sc]
                    visited[nr][nc] = 1
                    DFS(sr, sc, nr, nc, cnt+tmp)
                    # DFS 보낸 다음 visited와 town 상태 원상 복귀
                    town[nr][nc] = backup
                    visited[nr][nc] = 0
                # 가려는 곳의 확진자가 같거나 많다면 추가 감염자 없이 누적, DFS 보낸 다음 visited 상태 원상 복귀
                else:
                    visited[nr][nc] = 1
                    DFS(sr, sc, nr, nc, cnt)
                    visited[nr][nc] = 0

T = int(input())
for t in range(1, T+1):
    N = int(input())
    town = [list(map(int, input().split())) for _ in range(N)]
    min_patients = 0
    visited = [[0]*N for _ in range(N)]
    for r in range(0, N):
        for c in range(0, N):
            if town[r][c] != -1:
                min_tmp = 987654321
                copy_town = []
                DFS(r, c, r, c, 0)
                min_patients += min_tmp
                town = copy.deepcopy(copy_town)
                town[r][c] = 0

    print("#%d %s" % (t, min_patients))