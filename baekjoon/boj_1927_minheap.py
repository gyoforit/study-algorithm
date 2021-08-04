import sys, heapq
input = sys.stdin.readline
N = int(input())
heap = []
answer = []
for _ in range(N):
    i = int(input())
    if not i:
        if not heap:
            answer.append(0)
        else:
            tmp = heapq.heappop(heap)
            answer.append(tmp)
    else:
        heapq.heappush(heap, i)

for ans in answer:
    print(ans)