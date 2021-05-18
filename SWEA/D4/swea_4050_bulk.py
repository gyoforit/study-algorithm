T = int(input())
for t in range(1, T+1):
    N = int(input())
    tags = sorted(list(map(int, input().split())), reverse=True)
    sale = 0
    for i in range(2, N, 3):
        sale += tags[i]
    print("#%d %d" % (t, sum(tags)-sale))