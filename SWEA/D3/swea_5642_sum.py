'''
DP 문제! 바로 앞까지의 최적해에 나 자신을 더한 값 / 나 자신 중 최댓값 구하기
'''
T = int(input())
for t in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    dp = [0]*N
    dp[0] = nums[0]
    for i in range(1, N):
        dp[i] = max(nums[i], dp[i-1]+nums[i])

    print("#%d %d" % (t, max(dp)))