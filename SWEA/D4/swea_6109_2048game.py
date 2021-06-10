def game(n, dir):
    result = []
    if dir in ['left', 'right']:
        arr = grid
    elif dir in ['up', 'down']:
        arr = list(zip(*grid))

    if dir in ['left', 'up']:
        for r in arr:
            tmp = []
            for num in r:
                if not num:
                    continue
                else:
                    if not tmp:
                        tmp.append(num)
                    else:
                        if num == tmp[-1]:
                            tmp[-1] *= 2
                            tmp.append(0)
                        else:
                            tmp.append(num)
            new_tmp = [i for i in tmp if i]
            new_tmp = new_tmp + [0] * (n - len(new_tmp))
            result.append(new_tmp)

    elif dir in ['right', 'down']:
        for r in arr:
            tmp = []
            for num in r[::-1]:
                if not num:
                    continue
                else:
                    if not tmp:
                        tmp.append(num)
                    else:
                        if num == tmp[-1]:
                            tmp[-1] *= 2
                            tmp.append(0)
                        else:
                            tmp.append(num)
            new_tmp = [i for i in tmp if i]
            new_tmp = [0] * (n - len(new_tmp)) + new_tmp[::-1]
            result.append(new_tmp)

    return result

T = int(input())
for t in range(1, T + 1):
    N, D = input().split()
    grid = [list(map(int, input().split())) for _ in range(int(N))]
    ans = game(int(N), D)
    if D in ['up', 'down']:
        ans = list(zip(*ans))
    print("#%d" % t)
    for r in ans:
        print(*r)