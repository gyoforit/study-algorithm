num = 1000000007
T = int(input())
for t in range(1, T+1):
    check = input()
    case = [[0]*16 for _ in range(len(check))]
    for i in range(len(check)):
        # 모든 경우의 수 (다 안오는 경우는 제외)
        for k in range(1, 16):
            # 첫날일 때 - A는 반드시 참여
            if i == 0:
                case[i][k] = (k & 1) and (k & (1 << ord(check[i])-65))
            else:
                case[i][k] = (case[i-1][k] + (k & (1 << ord(check[i])-65)))%num

    print("#%d %d" % (t, sum(case[-1])%num))