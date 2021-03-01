# 210213
# 이것이 코딩 테스트다_그리디
# 실전 문제
# 실전 2. 큰 수의 법칙
# break의 위치!!!!
def bubble_sort(n):
    for i in range(len(n)-1, -1, -1): # 끝값
        for j in range(0, i):
            if n[j] > n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]
    return n

N, M, K = map(int, input().split())
num = list(map(int, input().split()))
cnt = 0
total = 0
bubble_sort(num)
# 반복 돌 때 항상 cnt == M 인지 먼저 확인을 해야 반복문을 빠져나갈지 말지 결정 가능
while True:
    for i in range(K):
        if cnt == M:
            break
        total += num[N-1]
        cnt += 1
    if cnt == M:
        break
    total += num[N-2]
    cnt += 1
print(total)
# 다른풀이: 가장 큰 수가 더해지는 횟수, 두번째 큰 수가 더해지는 횟수 따로 세서..

# 실전 3. 숫자 카드 게임
'''
행 별 min number을 구한 다음
max number과 비교하여 더 크면 교체
-> min number 중에서 가장 큰 값 출력
'''
N = 세로 M = 가로
N, M = map(int, input().split())
max_num = 0
for i in range(N): # N번 반복
    row = list(map(int, input().split()))
    min_num = row[0]
    for i in range(M):
        if row[i] < min_num:
            min_num = row[i]
    if min_num > max_num:
        max_num = min_num
print(max_num)

# 실전4. 1이 될 때까지
'''
N이 1이 될 때까지 K로 나눠지면 나눈 후 cnt +1
K로 나눠지지 않으면 -1 한 후에 cnt +1
계속 반복
'''
N, K = map(int, input().split())
cnt = 0
while True:
    if N == 1:
        break
    if N % K == 0:
        N = N//K
        cnt += 1
    else:
        N -= 1
        cnt += 1
print(cnt)
# 다른 풀이: N이 k보다 작아질 때 까지 계속 나누기 -> 나중에 1은 한번에 빼기

# 유형별 기출
# 1. 모험가 길드
# 그룹 수가 최대가 되려면? 최소 인원만 모이면 바로 그룹 생성
N = int(input())
nums = list(map(int, input().split()))
cnt = [0] * 100001 # 공포도별 모험가 개수 세는용
ans = 0
for n in nums:
    cnt[n] += 1

for idx in range(1, len(cnt)): # 1부터 100,000
    if cnt[idx] >= idx:
        ans += cnt[idx]//idx

print(ans)

# cnt 없이 푸는 법
nums.sort()
ans = 0
cnt = 0
for n in nums: # 정렬된 공포도 리스트를 하나씩 돌며
    cnt += 1 # count에 추가
    if cnt >= n: # 해당 공포도 수 이상이 되면
        ans += 1 # 그룹 하나 생성 후
        cnt = 0 # cnt는 다시 0으로 초기화

# 2. 곱하기 혹은 더하기
# 만약 0이면? 그 다음걸 더하기. 아니면 계속 곱하기
N = input()
result = 0
for n in N:
    if int(n) == 0 or result == 0:
        result += int(n)
    else:
        result *= int(n)
print(result)
# -> 예시 input은 통과했으나, 고려하지 못한 것 = 1!!
# 0처럼 1일 때도 곱하는 것 보다 더하는게 더 나음
N = input()
result = 0
for n in N:
    if int(n) <= 1 or result <= 1:
        result += int(n)
    else:
        result *= int(n)
print(result)

# 3. 문자열 뒤집기(백준 #1439)
'''
0이 연속하는 구간 / 1이 연속하는 구간을 각각 count
더 적은 쪽을 바꾸는 것으로 선택!
'''
S = input()
zero = 0
one = 0
now = -1
for s in S:
    if int(s) != now:
        if int(s) == 0:
            now = int(s)
            zero += 1
        else:
            now = int(s)
            one += 1
result = 0
if zero > one:
    result = one
else:
    result = zero
print(result)

# 210214
# 4. 만들 수 없는 금액
'''
그리디 문제 중 가장 풀이법 생각하기 어려웠음! 나중에 꼭 다시 풀어보기
'''
N = int(input())
num = list(map(int, input().split()))
num.sort()
target = 1
for n in num:
    if n > target:
        break
    target += n
print(target)

# 5. 볼링공 고르기
N, M = map(int, input().split())
ball = list(map(int, input().split()))
cnt = 0
for i in range(0, len(ball)-1):
    for j in range(i+1, len(ball)):
        if ball[i] != ball[j]:
            cnt += 1
print(cnt)
# 다른 풀이: 무게별로 count하기
N, M = map(int, input().split())
ball = list(map(int, input().split()))
array = [0] * 11
for b in ball:
    array[b] += 1
result= 0
for i in range(1, M+1):
    N -= array[i]
    result += array[i]*N
print(result)

# 210228
# 이것이 코딩 테스트다_구현
# 예제 1. 상하좌우
# 이중 리스트 - 패딩 사용해서 인덱스 접근 용이하게..
# 델타로도 풀 수 있을듯!
N = int(input())
map = [[0]*(N+2)]
for _ in range(N):
    map.append([0]+([1]*N)+[0])
map.append([0]*(N+2))
move = list(input().split())
r, c = 1, 1
for m in move:
    if m == 'L':
        if map[r][c-1] != 0:
            c -= 1
    elif m == 'R':
        if map[r][c+1] != 0:
            c += 1
    elif m == 'U':
        if map[r-1][c] != 0:
            r -= 1
    else:
        if map[r+1][c] != 0:
            r += 1
print(r, c, end=' ')

# 예제 2. 시각
# 완전탐색!
cnt = 0
N = int(input())
for h in range(N+1):
    for m in range(0, 60):
        for s in range(0, 60):
            if '3' in str(s) or '3' in str(m) or '3' in str(h):
                cnt += 1
print(cnt)

# 210301
# 실전 2. 왕실의 나이트
board = [[0]*10]
for _ in range(8):
    board.append([0]+([1]*8)+[0])
board.append([0]*10)
drc = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]
now = input()
r, c = ord(now[0])-96, int(now[1])
cnt = 0
for i in range(8):
    dr = drc[i][0]
    dc = drc[i][1]
    if r+dr > 1 and r+dc > 1 and board[r+dr][c+dc] == 1:
        cnt += 1
print(cnt)