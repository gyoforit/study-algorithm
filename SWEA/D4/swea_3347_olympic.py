T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    sports, judges = list(map(int, input().split())), list(map(int, input().split()))
    cnt = [0]*N
    for j in range(M):
        for s in range(N):
            if sports[s] <= judges[j]:
                cnt[s] += 1
                break
    result = cnt.index(max(cnt))
    print("#%d %d" % (t, result+1))