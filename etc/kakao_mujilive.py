# [카카오 기출] 무지의 먹방 라이브
# 정확도는 거의 맞는데 효율성 0
from collections import deque
def solution(food_times, k):
    queue = deque()
    for idx, t in enumerate(food_times):
        queue.append((idx, t))

    cnt = 0
    while cnt < k:
        cnt += 1
        i, target = queue.popleft()
        target -= 1
        if target > 0:
            queue.append((i, target))

    answer = queue[0][0]+1 if len(queue) > 0 else -1
    return answer