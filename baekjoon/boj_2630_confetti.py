# r, c 색종이의 시작좌표 / n 색종이의 길이
def check(r, c, n):
    flag = 0
    for i in range(r, r+n):
        for j in range(c, c+n):
            if confetti[i][j] != confetti[r][c]:
                check(r, c, n//2)
                check(r+(n//2), c, n//2)
                check(r, c+(n//2), n//2)
                check(r+(n//2), c+(n//2), n//2)
                flag = 1
                break
        if flag:
            break
    else:
        if confetti[r][c] == 1:
            ans[1] += 1
        else:
            ans[0] += 1
    return
N = int(input())
confetti = [list(map(int, input().split())) for _ in range(N)]
ans = [0, 0]
check(0, 0, N)
for a in ans:
    print(a)