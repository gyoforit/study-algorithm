# 범위가 256이 최대이기 때문에 0~256 완전탐색
import sys
input = sys.stdin.readline
N, M, B = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]
min_time = 987654321987654321
min_height = 0
for size in range(257):
    plus = 0 # 깎는 블럭 수(2초)
    minus = 0 # 채우는 블럭 수
    for r in range(N):
        for c in range(M):
            gap = ground[r][c]-size
            if gap > 0: # 깎기
                plus += gap
            elif gap < 0: # 채우기
                minus += -gap
    total = B + plus - minus
    if total < 0: continue
    total_time = plus*2+minus
    if total_time <= min_time:
        min_time = total_time
        min_height = size

print(min_time, min_height)

