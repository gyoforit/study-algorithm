N = int(input())
ans = 0
cnt = 0
while True:
    if '666' in str(ans):
        cnt += 1
        if cnt == N:
            print(ans)
            break
    ans += 1