# 투포인터 활용
# 고기양이 목표보다 적으면 오른쪽으로 하나 추가(+1 이동)
# 목표보다 많으면 왼쪽을 하나 덜어내기(+1 이동)
N, M = map(int, input().split())
fish = list(map(int, input().split()))
left, right = 0, 0
cnt = 0
now = 0
while left < N:
	if right < N and now < M:
		now += fish[right]
		right += 1
	else:
		now -= fish[left]
		left += 1
	if now == M:
		cnt += 1
print(cnt)