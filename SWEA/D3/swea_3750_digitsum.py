result = []
T = int(input())
for _ in range(1, T+1):
    num = input()
    while len(num) > 1:
        tmp = 0
        for n in num:
            tmp += int(n)
        num = str(tmp)
    result.append(num)

for idx, r in enumerate(result, start=1):
    print("#%d %s" % (idx, r))

# 재귀로 풀 때 return 값 주의!
def solution(num):
    if len(num) == 1:
        return num
    tmp = 0
    for n in num:
        tmp += int(n)
    return solution(str(tmp))