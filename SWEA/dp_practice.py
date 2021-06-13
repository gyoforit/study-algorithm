import sys
sys.stdin = open('input_dp_1.txt')

def DP(k): # k에서의 최고 점수
    if k < 0:
        return -987654321
    elif k == 0:
        return 0
    else:
        max_score[k] = max(DP(k-2), DP(k-7))+road[k]
    return max_score[k]


n = int(input())
road = list(map(int, input().split())) + [0]*100
max_score = [0]*100
result = -987654321
for i in range(0, 6):
    tmp = DP(n+i)
    result = max(result, tmp)
print(max_score)
print(result)
