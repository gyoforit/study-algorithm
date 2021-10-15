N = int(input())
stones = list(map(int, input().split())) + [0]
DP = [0]*(N+1)
for i in range(N+1):
	if i <= 2:
		DP[i] = stones[i]
	else:
		DP[i] = min(stones[i]+DP[i-1], stones[i]+DP[i-2], stones[i]+DP[i-3])
print(DP[N])