import sys, heapq
sys.stdin = open('input.txt')
heap = []
N = int(input())
result = []
for _ in range(N):
    x = int(input())
    if not x:
        if heap:
            tmp = heapq.heappop(heap)
            result.append(tmp[1])
        else:
            result.append(0)
    else:
        heapq.heappush(heap, (abs(x), x))

for r in result:
    print(r)