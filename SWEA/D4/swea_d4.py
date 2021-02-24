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