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

# 1219. [S/W 문제해결 기본] 4일차 - 길찾기
V = 100
# 경로 탐색하는 함수 정의
def DFS(V, AL, sv):
    visited = [0]*V
    stack = [sv]
    while stack:
        now = stack.pop(-1)
        if visited[now] == 0:
            visited[now] = 1
            # 99까지 갈 수 있는지의 여부가 중요하기 때문에 99까지 닿으면 return 1
            if now == 99:
                return 1
            for i in AL[now]:
                if not visited[i]:
                    stack.append(i)
    # 중간에 return 없이 다 돌았으면 경로 없다는 뜻이므로 return 0
    return 0

for _ in range(10):
    N, E = map(int, input().split())
    route = list(map(int, input().split()))
    edges = [(route[i], route[i+1]) for i in range(0, E*2, 2)]
    AL =[[] for _ in range(V)]
    for s, e in edges:
        AL[s].append(e)

    result = DFS(V, AL, 0)
    print("#%d %d" % (N, result))

# 210224
# 1223. [S/W 문제해결 기본] 6일차 - 계산기2
# 연산자의 우선순위를 반환하는 함수
def priority(x):
    if x == '+' or x == '-':
        return 2
    elif x == '*' or x == '/':
        return 1

# 후위표기법으로 변환해주는 함수
def postfix(S):
    after = ''
    stack = []
    for s in S:
        if s not in '*/+-()':
            after += s
        else:
            # '('는 stack 안에서 우선순위 가장 낮으므로 무시(?)하고 다른거 append 하게 처리
            if not stack or s == '(' or stack[-1] == '(':
                stack.append(s)
            elif s == ')':
                while True:
                    if stack[-1] == '(':
                        stack.pop()
                        break
                    after += stack.pop()
            elif s in '+-*/':
                if priority(s) < priority(stack[-1]):
                    stack.append(s)
                else:
                    while True:
                        # 인덱스 에러 방지: stack이 비었을 때도 고려함
                        if not stack or priority(s) < priority(stack[-1]):
                            break
                        after += stack.pop()
                    stack.append(s)
    # 수식의 끝까지 도달한 후, stack이 빌 때까지 계속 pop
    while stack:
        after += stack.pop()
    return after

# 후위표기법을 계산하는 함수
def cal(A):
    stack = []
    for a in A:
        if a not in '+-*/':
            stack.append(a)
        else:
            # 피연산자를 미리 int로 바꿔놓음
            y = int(stack.pop())
            x = int(stack.pop())
            if a == '+':
                ans = x+y
            elif a == '-':
                ans = x-y
            elif a == '*':
                ans = x*y
            else:
                ans = x/y
            stack.append(ans)
    return stack.pop()

for t in range(1, 11):
    L = int(input())
    S = input()
    result = cal(postfix(S))

    print("#%d %d" % (t, result))

# 4408. 자기 방으로 돌아가기
# 출발점 > 도착점 인 경우를 고려하자!

T = int(input())
for t in range(1, T+1):
    # (1, 2) (3, 4) 등 둘씩 짝을 지어 복도를 공유하므로 겹치는 경로 체크할 배열 크기는 200
    room = [0]*201
    N = int(input())
    for _ in range(N):
        s, e = map(int, input().split())
        # 출발점 > 도착점인 경우 편의상 둘을 바꿈
        if s > e:
            s, e = e, s
        # s, e가 홀수인 경우 짝수로 보정
        if s % 2:
            s += 1
        if e % 2:
            e += 1
        # 각 학생별로 지나는 경로에 +1
        for i in range(s//2, (e//2)+1):
            room[i] += 1
    # 가장 많이 겹친 수만큼 시간이 걸릴 것!
    time = max(room)
    print("#%d %d" % (t, time))

# 1224. [S/W 문제해결 기본] 6일차 - 계산기3
# 전에 제출한 코드가 이 문제에선 오류가 나서 우선순위를 dictionary로 수정함
isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}

# 후위표기법으로 변환해주는 함수
def postfix(S):
    after = ''
    stack = []
    for s in S:
        if s.isdigit():
            after += s
        elif s == ')':
            while True:
                if stack[-1] == '(':
                    stack.pop()
                    break
                after += stack.pop()
        else:
            if not stack or s == '(' or icp.get(s) > isp.get(stack[-1]):
                stack.append(s)
            else:
                while True:
                    if not stack or icp.get(s) > isp.get(stack[-1]):
                        break
                    after += stack.pop()
                stack.append(s)
    # 수식의 끝까지 도달한 후, stack이 빌 때까지 계속 pop
    while stack:
        after += stack.pop()
    return after

# 후위표기법을 계산하는 함수
def cal(A):
    stack = []
    for a in A:
        if a not in '+-*/':
            stack.append(a)
        else:
            y = int(stack.pop())
            x = int(stack.pop())
            if a == '+':
                ans = x+y
            elif a == '-':
                ans = x-y
            elif a == '*':
                ans = x*y
            else:
                ans = x/y
            stack.append(ans)
    return stack.pop()

for t in range(1, 11):
    L = int(input())
    S = input()
    result = cal(postfix(S))

    print("#%d %d" % (t, result))

# 210304
# 1226. [S/W 문제해결 기본] 7일차 - 미로1
drc = [[1, 0], [-1, 0], [0, 1], [0, -1]]
def BFS_maze(sr, sc):
    visited = [[0]*16 for _ in range(16)]
    queue = [(sr, sc)]
    visited[sr][sc] = True
    while queue:
        tr, tc = queue.pop(0)
        if maze[tr][tc] == 3:
            return 1
        for i in range(4):
            nr = tr+drc[i][0]
            nc = tc+drc[i][1]
            if maze[nr][nc] != 1 and visited[nr][nc] == 0:
                visited[nr][nc] = True
                queue.append((nr, nc))
    return 0

for _ in range(10):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    for r in range(16):
        for c in range(16):
            if maze[r][c] == 2:
                sr, sc = r, c
    result = BFS_maze(sr, sc)

    print("#%d %d" % (N, result))

# 210305
# 1258. [S/W 문제해결 응용] 7일차 - 행렬찾기
drc = [[1, 0], [0, 1]]

# 행렬을 탐색하는 함수 - 항상 좌상단 모서리에서 시작하기 때문에 델타는 (우,하)방향만 존재
def BFS_search(r, c):
    global visited
    er, ec = r, c
    queue = [(r, c)]
    while queue:
        tr, tc = queue.pop(0)
        for dr, dc in drc:
            nr, nc = tr+dr, tc+dc
            if 0<=nr<=N-1 and 0<=nc<=N-1:
                if changgo[nr][nc] != 0:
                    changgo[nr][nc] = 0
                    queue.append((nr, nc))
                    if nr > er: er = nr
                    if nc > ec: ec = nc
    height = er-r+1
    width = ec-c+1
    return height, width

T = int(input())
for t in range(1, T+1):
    N = int(input())
    changgo = [list(map(int, input().split())) for _ in range(N)]
    matrix = []
    for r in range(N):
        for c in range(N):
            if changgo[r][c] != 0:
                h, w = BFS_search(r, c)
                matrix.append((h, w, h*w))
    # 여러가지 기준으로 정렬할 땐 sorted의 key를 사용
    matrix = sorted(matrix, key=lambda x : (x[2], x[0]))
    result = []
    for H, W, S in matrix:
        result.append(H)
        result.append(W)
    print("#%d %d %s" % (t, len(matrix), ' '.join(map(str, result))))

# 4613. 러시아 국기 같은 깃발
# 중복 순열!
def perm(idx, S):
    global ans
    # 유망성 검사 - 이후 작업은 의미 없으니까 가지치기
    if S > N:
        return

    # 세가지 색깔이 각각 몇줄인지 결정 되면
    if idx == 3:
        if S == N:
            cnt = 0 # 바꿔야 하는 칸 개수를 담음

            # 구분하는 지점
            st = sel[0]
            st2 = st + sel[1]

            # 흰색이 아닌 칸에 흰색 칠하기
            for i in flag[:st]:
                for j in i:
                    if j != 'W':
                        cnt += 1

            # 파란색 칠하기
            for i in flag[st:st2]:
                for j in i:
                    if j != 'B':
                        cnt += 1

            # 빨간색 칠하기
            for i in flag[st2:]:
                for j in i:
                    if j != 'R':
                        cnt += 1

            # 최솟값이면 갱신
            if cnt < ans:
                ans = cnt
        return

    for i in range(1, N-1): #각각 한 줄씩은 보장해야 하니까 1부터 시작!
        sel[idx] = i
        perm(idx+1, S+i)

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]
    # W, B, R을 각각 몇줄씩 칠할지 결정하는 sel
    sel = [0]*3
    ans = 10000000

    # idx, 중간 합(몇줄을 뽑았는지)
    perm(0, 0)

    print("#%d %d" % (t, ans))
    
# 210311
# 1952. [모의 SW 역량테스트] 수영장
'''
DP로 접근!
'''
def get_min(n): # n월까지의 최소요금
    if n == 1:
        return min(plan[n]*d, m, q, y)
    elif n == 2:
        return min(get_min(1)+min(plan[n]*d, m), q, y)
    elif n == 3:
        return min(get_min(2)+min(plan[n]*d, m), q, y)
    else:
        return min(get_min(n-1)+min(plan[n]*d, m), get_min(n-2)+q, get_min(n-3)+q, y)

T = int(input())
for t in range(1, T+1):
    d, m, q, y = map(int, input().split())
    plan = [0] + list(map(int, input().split()))
    result = get_min(12)
    print("#%d %d" % (t, result))