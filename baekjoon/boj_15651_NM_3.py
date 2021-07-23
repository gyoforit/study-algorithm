# 중복순열
def comb(lv, nums):
    if lv == M:
        print(*nums)
        return
    # 중복 허용이므로 범위를 전범위로 설정
    for i in range(0, N):
        # 넣은 후 다음 레벨로 보내고
        nums.append(i+1)
        comb(lv+1, nums)
        # 중복을 위해 다시 빼기
        # 순열이기 때문에 맨 마지막 요소를 빼줌
        nums.pop()

N, M = map(int, input().split())
comb(0, [])