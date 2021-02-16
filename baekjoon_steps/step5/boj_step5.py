# 백준 5단계 - 1차원 배열
# 210214
# 10818. 최소, 최대
N = int(input())
num = list(map(int, input().split()))
mx = num[0]
mn = num[0]
for i in num:
    if i > mx:
        mx = i
    elif i < mn:
        mn = i
print('%d %d' % (mn, mx))

# 2562. 최댓값
num = []
for i in range(9):
    num += [int(input())]
max_idx = 0
for i in range(len(num)):
    if num[max_idx] < num[i]:
        max_idx = i
print(num[max_idx])
print(max_idx+1)

# 2577. 숫자의 개수
A = int(input())
B = int(input())
C = int(input())
result = str(A*B*C)
cnt = [0] * 10
for i in result:
    cnt[int(i)] += 1

for j in cnt:
    print(j)

# 3052. 나머지
num = []
for t in range(10):
    num += [int(input())]
result = []
for i in num:
    result += [i%42]
result = list(set(result))
cnt = 0
for j in result:
    cnt += 1
print(cnt)

#1546. 평균
N = int(input())
score = list(map(int, input().split()))
max_s = score[0]
for i in score:
    if i > max_s:
        max_s = i
total = 0
for j in score:
    total += (j/max_s)*100
print(total/N)

# 8958. OX퀴즈
T = int(input())
for t in range(1, T+1):
    N = input()
    score = 0
    cnt = 1
    for i in N:
        if i == 'O':
            score += cnt
            cnt += 1
        else:
            cnt = 1
    print(score)