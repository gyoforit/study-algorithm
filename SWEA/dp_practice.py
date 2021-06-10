import sys
sys.stdin = open('input_dp_1.txt')

def DP(n): # n칸에서의 최고 점수
    if max_score[n]:
        return max_score[n]

    a = DP(n-7)+road[n]
    b = DP(n-2)+road[n]
    print(max_score)
    print(a)
    print(b)
    road[n] = max(a, b)
    return

n = int(input())
road = list(map(int, input().split()))
max_score = [0]*(n)
for i in range(0, 8):
    max_score[i] = road[i]
DP(n-1)

print(max_score)
