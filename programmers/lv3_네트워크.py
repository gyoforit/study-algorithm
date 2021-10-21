from collections import deque

def solution(n, computers):
    def bfs(start):
        nonlocal answer
        answer += 1
        queue = deque()
        queue.append(start)
        checked[start] = 1
        while queue:
            target = queue.popleft()
            for i in range(n):
                if i != target and computers[target][i] and not checked[i]:
                    checked[i] = 1
                    queue.append(i)

    answer = 0
    checked = [0] * n
    for c in range(n):
        if not checked[c]:
            bfs(c)

    return answer