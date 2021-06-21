# 이분탐색 응용
# 구해야 할 것: 랜선 개수가 최대가 되는 랜선의 길이
# 범위: 1~주어진 랜선 중 최댓값
K, N = map(int, input().split())
cables = []
for _ in range(K):
    cables.append(int(input()))
l, r = 1, max(cables)
while l <= r:
    mid = (l+r)//2
    cnt = sum([cable//mid for cable in cables])
    # 개수가 모자르면 길이를 더 작게 해야함
    if cnt < N:
        r = mid-1
    # 개수가 더 많으면 길이를 더 늘여도 됨
    elif cnt >= N:
        l = mid+1
        result = mid
print(result)