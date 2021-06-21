# 이분탐색 복습
# l > r 이 되기 전까지 탐색한다 (l==r인 경우도 탐색)
def binary_search(x, arr):
    l, r = 0, len(arr)-1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == x:
            return 1
        elif arr[mid] > x:
            r = mid-1
        elif arr[mid] < x:
            l = mid+1
    return 0

N = int(input())
nums = sorted(list(map(int, input().split())))
M = int(input())
target = list(map(int, input().split()))
result = []
for t in target:
    result.append(binary_search(t, nums))
for i in result:
    print(i)