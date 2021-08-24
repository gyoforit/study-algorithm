def solution(sticker):
    answer = []
    L = len(sticker)
    dp = [0] * L
    if L == 1:
        return sticker[0]
    # 첫번째 스티커 뜯음
    dp[0] = sticker[0]
    dp[1] = sticker[0]
    for i in range(2, L - 1):
        dp[i] = max(dp[i - 2] + sticker[i], dp[i - 1])
    answer.append(max(dp))

    # 첫번째 스티커 안 뜯음
    dp2 = [0] * L
    dp2[1] = sticker[1]
    for i in range(2, L):
        dp2[i] = max(dp2[i - 2] + sticker[i], dp2[i - 1])
    answer.append(max(dp2))

    return max(answer)