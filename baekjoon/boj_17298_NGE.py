from collections import deque
N = int(input())
nums = list(map(int, input().split()))
NGE = [-1]*N
stack = deque()
for i, n in enumerate(nums):
    while stack and stack[-1][1] < n:
        idx, num = stack.pop()
        NGE[idx] = n

    stack.append((i, n))

print(*NGE)