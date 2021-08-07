import sys
from collections import Counter
sys.stdin = open('input.txt')

N = int(input())
nums = list(map(int, input().split()))
num_dict = Counter(nums)
nums = sorted(list(set(nums)))
M = int(input())
targets = list(map(int, input().split()))
ans = []
for t in targets:
    l, r = 0, len(nums)-1
    while l <= r:
        mid = (l+r)//2
        if nums[mid] == t:
            ans.append(num_dict[t])
            break
        elif nums[mid] > t:
            r = mid-1
        else:
            l = mid+1
    else:
        ans.append(0)
print(nums)
print(num_dict)
print(*ans)