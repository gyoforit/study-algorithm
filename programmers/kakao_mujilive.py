# [카카오 기출] 무지의 먹방 라이브
# 재도전: 우선순위큐를 활용한 그리디
import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    heap = []
    for idx, food in enumerate(food_times, start=1):
        heapq.heappush(heap, (food, idx))
    # 바퀴수(전체힙을 몇 번 돌았는지), 누적 먹은 시간
    cnt, time_eat = 0, 0
    while True:
        # 힙의 첫 요소를 다 먹는 시간 > 남은 시간 이라면 break
        if (heap[0][0]-cnt)*len(heap) > k-time_eat:
            break
        food, idx = heapq.heappop(heap)
        # pop한 요소를 다 먹는데 걸리는 시간
        total_time = (food-cnt)*(len(heap)+1)
        cnt += food-cnt
        time_eat += total_time

    heap.sort(key=lambda x: x[1])
    answer = heap[(k-time_eat)%len(heap)][1]
    return answer

# solution([8, 4, 6], 15)
# solution([3, 1, 2], 5)
# print(solution([1, 10, 8, 4, 5, 9, 2], 60))

# 첫 시도: 정확도는 거의 맞는데 효율성 0
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