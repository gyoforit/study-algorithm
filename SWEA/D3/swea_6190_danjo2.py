# 미완성
def isdanjo(num):
    num = str(num)
    for i in range(len(num)-1):
        if num[i] > num[i+1]:
            return False
    return True

T = int(input())
for t in range(1, T+1):
    N = int(input())
    nums = sorted(list(map(int, input().split())), reverse=True)
    # print(nums)
    mx = -1
    for i in range(N-1):
        tmp = nums[i]*nums[i+1]
        if tmp <= mx:
            break
        if isdanjo(tmp):
            mx = max(mx, tmp)
            break

    print("#%d %d" % (t, mx))