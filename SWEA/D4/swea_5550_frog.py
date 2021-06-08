T = int(input())
for t in range(1, T+1):
    frogs = list(input())
    cnt = 0
    tmp = []
    while True:
        to_change = []
        flag = 0
        for i in range(len(frogs)):
            if not tmp and frogs[i] == 'c':
                tmp.append('c')
                to_change.append(i)
            elif frogs[i] == 'r' and tmp and tmp[-1] == 'c':
                tmp.append('r')
                to_change.append(i)
            elif frogs[i] == 'o' and tmp and tmp[-1] == 'r':
                tmp.append('o')
                to_change.append(i)
            elif frogs[i] == 'a' and tmp and tmp[-1] == 'o':
                tmp.append('a')
                to_change.append(i)
            elif frogs[i] == 'k' and tmp and tmp[-1] == 'a':
                to_change.append(i)
                tmp.clear()
                flag = 1
                for j in to_change:
                    frogs[j] = 'X'
                to_change.clear()
        if flag:
            cnt += 1
        else:
            break
    if cnt == 0 or frogs.count('X') != len(frogs):
        cnt = -1
    print("#%d %d" % (t, cnt))