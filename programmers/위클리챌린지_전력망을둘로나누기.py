from copy import deepcopy
from collections import deque


def solution(n, wires):
    wires = [[]] + wires
    # 전력망 자르는 함수
    def cut_wire(a, b):
        new_AL = deepcopy(AL)
        new_AL[a].remove(b)
        new_AL[b].remove(a)
        return new_AL

    # 연결된 전력망 길이 구하는 함수
    def bfs(arr, start):
        cnt = 0
        visited = [0] * (n + 1)
        queue = deque()
        visited[start] = 1
        queue.append(start)
        cnt += 1
        while queue:
            target = queue.popleft()
            nodes = arr[target]
            for node in nodes:
                if not visited[node]:
                    visited[node] = 1
                    queue.append(node)
                    cnt += 1
        return cnt

    answer = 987654321
    # 인접리스트 구하기
    AL = [[] for _ in range(n + 1)]
    for i in range(1, len(wires)):
        v1, v2 = wires[i][0], wires[i][1]
        AL[v1].append(v2)
        AL[v2].append(v1)
        
    # 연결된 전력 하나씩 끊어보면서 전선길이의 차이 구하기
    for i in range(1, len(wires)):
        v1, v2 = wires[i][0], wires[i][1]
        tmp = cut_wire(v1, v2)
        cnt_1 = bfs(tmp, v1) - 1
        cnt_2 = bfs(tmp, v2) - 1
        answer = min(answer, abs(cnt_1 - cnt_2))
    return answer