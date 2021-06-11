T = int(input())
for t in range(1, T+1):
    before = input()
    after = input()
    calc = [(1, 1), (3, 2), (5, 4), (7, 6)]
    result = 0
    for i in range(4):
        # 양수라면 after의 알파벳 순서가 더 늦은 것 -> 반시계 방향으로 돌려야 함
        tmp = ord(after[i])-ord(before[i])
        abs_tmp = abs(tmp)
        flag = 1 if tmp == abs_tmp else 0 # 양수-1-반시계방향, 음수면 0
        min_time = min(abs_tmp*calc[i][flag], (26-abs_tmp)*calc[i][abs(flag-1)])
        result += min_time
    print("#%d %s" % (t, result))
