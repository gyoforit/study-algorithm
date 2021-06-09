import sys, pprint
sys.stdin = open('input_4317.txt')

def check(r, c, cnt):
    global max_chip
    print(r, c, cnt)
    if c == W-2 and r == H-2:
        x, y, z, w = wafer[r][c], wafer[r][c + 1], wafer[r + 1][c], wafer[r + 1][c + 1]
        if x == 0 and y == 0 and z == 0 and w == 0:
            cnt += 1
        pprint.pprint(wafer)
        max_chip = max(max_chip, cnt)
        return

    if 0<=r<=H-2 and 0<=c<=W-2:
        x, y, z, w = wafer[r][c], wafer[r][c+1], wafer[r+1][c], wafer[r+1][c+1]
        nc = c + 1 if c + 1 <= W - 2 else 0
        nr = r if c + 1 <= W - 2 else r + 1
        if x == 0 and y == 0 and z == 0 and w == 0: # 가공가능: 가공 후 이동
            wafer[r][c], wafer[r][c+1], wafer[r+1][c], wafer[r+1][c+1] = 1, 1, 1, 1
            check(nr, nc, cnt+1)
            wafer[r][c], wafer[r][c + 1], wafer[r + 1][c], wafer[r + 1][c + 1] = 0, 0, 0, 0
        else: # 가공 불가능: +1칸 이동
            check(nr, nc, cnt)


T = int(input())
for t in range(1, T+1):
    H, W = map(int, input().split())
    wafer = [list(map(int, input().split())) for _ in range(H)]
    max_chip = 0
    check(0, 0, 0)
    # print("#%d %s" % (t, max_chip))
    # check(1, 0, 0)
    print("#%d %s" % (t, max_chip))
    # pprint.pprint(wafer)