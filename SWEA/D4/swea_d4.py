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

# 210218
# 3143. 가장 빠른 문자열 타이핑
T = int(input())
for t in range(1, T+1):
    A, B = input().split()
    result = len(A) - ((len(B)-1)*A.count(B))
    print(result+A.count(B))

# 5432. 쇠막대기 자르기
T = int(input())
for t in range(1, T+1):
    N = input()
    n = len(N)
    i = 0
    # pipe = 쇠막대기 / cut = 잘린 조각
    pipe = 0
    cut = 0
    while i < n:
        if N[i] == '(':
            # ( 다음 바로 )가 오면 레이저 -> 기존의 pipe 개수만큼 cut 증가
            if N[i+1] == ')':
                cut += pipe
                i += 2
            # )가 오지 않은 (는 pipe -> pipe 개수 +1
            else:
                pipe += 1
                i += 1
        # 둘다 아닌 )는 pipe의 끝 -> 레이저를 지나왔으므로 cut +1, pipe -1
        else:
            pipe -= 1
            cut += 1
            i += 1
    print("#%d %d" % (t, cut))