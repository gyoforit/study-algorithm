import heapq

T = int(input())
for t in range(1, T+1):
    N = int(input())
    heap = []
    result = []
    for _ in range(N):
        tmp = input().split()
        if tmp[0] == '1':
            heapq.heappush(heap, (-int(tmp[1]), int(tmp[1])))
        elif tmp[0] == '2':
            if len(heap) > 0:
                result.append((heapq.heappop(heap))[1])
            else:
                result.append(-1)
    print("#%d %s" % (t, ' '.join(map(str, result))))
