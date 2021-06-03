# 순열 말고 조합 구하듯이 풀면 됨
def dfs(lv, start):
    global nums
    if lv == M and len(nums) == M:
        print(*nums)
        return
    for i in range(start, N+1):
        nums.append(i)
        dfs(lv+1, i+1)
        nums.pop()


N, M = map(int, input().split())
nums = []
dfs(0, 1)