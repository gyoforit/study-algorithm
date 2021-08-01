import sys
sys.stdin = open('input.txt')
N = int(input())
liquids = sorted(list(map(int, input().split())))
l, r = 0, N-1
min_point = 2000000000
ans_a, ans_b = 0, 0
while l < r:
    tmp = liquids[l]+liquids[r]
    if abs(tmp) < abs(min_point):
        min_point = tmp
        ans_a = l
        ans_b = r
        if tmp == 0:
            break
    # 0과 가까워지기 위한 인덱스 조절
    # 0보다 큰 상태면 오른쪽부분을 줄어야
    if tmp > 0:
        r -= 1
    # 0보다 작은 상태면 왼쪽부분을 늘려야
    else:
        l += 1
print(liquids[ans_a], liquids[ans_b])