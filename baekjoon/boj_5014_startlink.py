from collections import deque
import sys
input = sys.stdin.readline
F, S, G, U, D = map(int, input().split())
dirs = [U, -D]
queue = deque()
queue.append((S, 0))
result = -1
# 똑같은 층 방문 방지를 위해 visited 배열 사용! set으로 해도 괜찮을듯
visited = [0]*F
visited[S-1] = 1
while queue:
    now, cnt = queue.popleft()
    if now == G:
        result = cnt
        break
    for dir in dirs:
        move = now+dir
        if dir != 0 and 1<=move<=F and not visited[move-1]:
            visited[move-1] = 1
            queue.append((move, cnt+1))

ans = result if result > -1 else 'use the stairs'
print(ans)