# 탐색 범위가 2000만 넘거나 데이터 개수가 1000만 이상이면 이진탐색 추천
# 탐색 범위가 1000억 이상이거나 데이터 개수 1000만 이상이면 input() 대신
# sys.stdin.readline().rstrip() 사용

def search(k):
    l = 0
    r = N-1
    while l <= r:
        mid = (l+r)//2
        if nums[mid] == k:
            return 'yes'
        elif nums[mid] < k:
            l = mid+1
        else:
            r = mid-1

    return 'no'

N = int(input())
nums = list(map(int, input().split()))
nums.sort()
M = int(input())
check = list(map(int, input().split()))
result = []
for m in check:
    result.append(search(m))

print(' '.join(result))