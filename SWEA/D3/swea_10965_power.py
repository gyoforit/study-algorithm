n = int((10000000)**0.5)
num = [True]*n
m = int(n**0.5)
for i in range(2, m+1):
    if num[i] == True:
        for j in range(i+i, n, i):
            num[j] = False
primelist = [i for i in range(2, n) if num[i] == True]

answer = []
T = int(input())
for t in range(1, T+1):
    a = int(input())
    result = 1
    if a**0.5 != int(a**0.5):
        for i in primelist:
            cnt = 0
            while a % i == 0:
                a //= i
                cnt += 1
            if cnt % 2:
                result *= i
            if a == 1 or i > a:
                break
        result *= a
    answer.append(result)

for idx, ans in enumerate(answer, start=1):
    print("#%d %d" % (idx, ans))