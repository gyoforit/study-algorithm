# 사전순으로 증가해야하므로 전에 넣은 수부터
def comb(lv, nums, start):
    if lv == M:
        print(*nums)
        return

    for i in range(start, N):
        nums.append(i+1)
        comb(lv+1, nums, i)
        nums.pop()

N, M = map(int, input().split())
comb(0, [], 0)