# 가장 첫 인덱스와 끝 인덱스 구해서 인덱스 차이만 구하면 된다.
def get_first(l, r, n, N):
    if l > r:
        return None
    mid = (l+r)//2
    if (nums[mid] == n) and (mid == 0 or nums[mid-1] < n):
        return mid
    elif nums[mid] < n:
        return get_first(mid+1, r, n, N)
    elif nums[mid] > n:
        return get_first(l, mid-1, n, N)

def get_last(l, r, n, N):
    if l > r:
        return None
    mid = (l+r)//2
    if (nums[mid] == n) and (mid == N-1 or nums[mid+1] > n):
        return mid
    elif nums[mid] < n:
        return get_last(mid+1, r, n, N)
    else:
        return get_last(l, mid-1, n, N)

def calc(f, l):
    if f and l:
        return l-f+1
    else:
        return -1
N, x = map(int, input().split())
nums = list(map(int, input().split()))
print(get_first(0, N-1, x, N))
print(get_last(0, N-1, x, N))
print(calc(get_first(0, N-1, x, N), get_last(0, N-1, x, N)))