import sys
N, M = map(int, input().split())
ricecake = list(map(int, input().split()))
ricecake.sort()
l, r = 0, ricecake[-1]
max_h = 0
while l <= r:
    mid = (l+r)//2
    cnt = 0
    for r in ricecake:
        if r > mid: cnt += r-mid
    if cnt == M:
        max_h = mid
        break
    elif cnt < M:
        r = mid-1
    else:
        max_h = mid # 최대한 덜 잘랐을 때가 정답이니까 기록해두기
        l = mid+1
print(max_h)