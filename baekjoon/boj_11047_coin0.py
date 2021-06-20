# 큰 동전부터 K보다 클 때 K를 동전으로 나눈 몫을 cnt에 더하기
# K는 나머지로 바꾸기
# 쭉... 0이 될 때까지
N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))
coins.sort(reverse=True)
cnt = 0
for coin in coins:
    if coin <= K:
        cnt += K//coin
        K %= coin
print(cnt)