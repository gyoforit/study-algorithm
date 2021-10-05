import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while (len(scoville) >=2) & (scoville[0] < K):
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        tmp = first + (second*2)
        heapq.heappush(scoville, tmp)
        answer += 1
    return answer if scoville[0] >= K else -1