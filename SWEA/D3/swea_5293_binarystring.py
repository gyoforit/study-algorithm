# 좀 더 정리할 수 있을듯
dic = {0: '00', 1: '01', 2: '10', 3: '11'}
def DFS(S):
    if nums.count(0) == len(nums):
        tmp.append(S)
        return
    if S[-1] == '1':
        if nums[3] > 0:
            nums[3] -= 1
            DFS(S+'1')
            nums[3] += 1
        elif nums[2] > 0:
            nums[2] -= 1
            DFS(S+'0')
            nums[2] += 1
    elif S[-1] == '0':
        if nums[0] > 0:
            nums[0] -= 1
            DFS(S+'0')
            nums[0] += 1
        elif nums[1] > 0:
            nums[1] -= 1
            DFS(S+'1')
            nums[1] += 1
    return

T = int(input())
for t in range(1, T+1):
    nums = list(map(int, input().split()))
    tmp = []
    for i in range(len(nums)):
        if nums[i] > 0:
            nums[i] -= 1
            DFS(dic.get(i))
            nums[i] += 1
    result = tmp[0] if len(tmp) >= 1 else 'impossible'
    print("#%d %s" % (t, result))