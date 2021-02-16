# 210216
# 1210. Ladder1
T = 10
for t in range(1, T+1):
    N = int(input())
    n = 100
    # 사다리 그려놓기
    ladder = [list(map(int, input().split())) for _ in range(n)]
    r = n-1
    c = 0
    # 왔던방향 (위 = 0, 왼쪽 = -1, 오른쪽 = 1) - 좌/우 이동할 때 쭉 한방향으로 가기 위해
    dir = 0
    # 마지막 행에서 2인 지점 찾기 (하나만 찾으면 됨)
    c = [i for i in range(n) if ladder[n-1][i] == 2]
    # r이 0이 되면(0행으로 돌아오면) 종료
    while r > 0:
        # 왼쪽으로 가기
        if (dir == 0 or dir == -1) and c > 0 and ladder[r][c-1] == 1:
            c -= 1
            dir = -1
        # 오른쪽으로 가기
        elif (dir == 0 or dir == 1) and c < n-1 and ladder[r][c+1] == 1:
            c += 1
            dir = 1
        # 위로 가기
        else:
            r -= 1
            dir = 0
    print("#%d %d" % (t, c))