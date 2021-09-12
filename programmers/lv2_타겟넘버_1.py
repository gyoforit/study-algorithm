from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append((0, 0))
    while queue:
        tmp, idx = queue.popleft()
        if idx == len(numbers) and tmp == target:
            answer += 1
        elif idx < len(numbers):
            plus = tmp + numbers[idx]
            minus = tmp - numbers[idx]
            queue.append((plus, idx + 1))
            queue.append((minus, idx + 1))

    return answer