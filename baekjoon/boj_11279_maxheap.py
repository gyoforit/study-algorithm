import sys, heapq
sys.stdin = open('input.txt')
heap = []
N = int(input())
result = []
for _ in range(N):
    num = int(input())
    if not num:
        if heap:
            ans = heapq.heappop(heap)
            result.append(ans[1])
        else:
            result.append(0)
    else:
        heapq.heappush(heap, (-num, num))

for r in result:
    print(r)