def isdanjo(num):
    for i in range(len(num)-1):
        if num[i] > num[i+1]:
            return False
    return True

def DFS(lv, start, total):
    global mx
    if lv == 2:
        if isdanjo(str(total)):
            mx = max(mx, total)
        return
    for i in range(start, N):
        DFS(lv+1, i+1, total*nums[i])

T = int(input())
for t in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    mx = -1
    DFS(0, 0, 1)
    print("#%d %d" % (t, mx))

