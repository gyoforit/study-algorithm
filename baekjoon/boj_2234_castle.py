drc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]
visited = [[0]*n for _ in range(m)]
# 방번호: 방크기 형식으로 저장한 dict
rooms = dict()
answer = []
room_no = 1
for r in range(m):
    for c in range(n):
        # 방문하지 않은 곳에서 BFS 시작
        if not visited[r][c]:
            queue = [(r, c)]
            visited[r][c] = room_no
            cnt = 1
            while queue:
                tr, tc = queue.pop(0)
                wall_info = bin(grid[tr][tc])[2:].zfill(4)
                for i in range(len(wall_info)):
                    # 벽이 아니고 범위 내라면 방문표시하고 queue에 넣기
                    if wall_info[i] == '0':
                        nr, nc = tr+drc[i][0], tc+drc[i][1]
                        if 0<=nr<m and 0<=nc<n and not visited[nr][nc]:
                            visited[nr][nc] = room_no
                            cnt += 1
                            queue.append((nr, nc))
            rooms[room_no] = cnt
            room_no += 1
answer.append(len(rooms))
answer.append(max(rooms.values()))
# 인접한 두 방 합칠 때의 최댓값 구하기
# 인접한 방 조건: 인접한 두 수의 값이 다를 때
max_cnt = 0
for r in range(m):
    for c in range(n):
        for dr, dc in drc:
            nr, nc = r+dr, c+dc
            if 0<=nr<m and 0<=nc<n:
                if visited[r][c] != visited[nr][nc]:
                    tmp = rooms[visited[r][c]]+rooms[visited[nr][nc]]
                    max_cnt = max(tmp, max_cnt)
answer.append(max_cnt)
print(visited)
for a in answer:
    print(a)
