# 210214
# 백준 4단계 - while문
# 10951. A+B - 4
while True:
    try:
        A, B = map(int, input().split())
    except:
        break
    print(A+B)

# 1110. 더하기 사이클
# string으로 변환할 때는 항상 int() 처리 먼저 해주기!
N = input()
cycle = 0
now = N
while True:
    if int(now) < 10:
        now = '0' + str(int(now))
    now = now[-1] + str(int(now[0])+int(now[1]))[-1]
    cycle += 1
    if int(now) == int(N):
        break
print(cycle)