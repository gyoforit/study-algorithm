N = int(input())
if N < 100:
    result = N
else:
    if N == 1000: N = 999
    cnt = 0
    for i in range(100, N+1):
        if int(str(i)[0])+int(str(i)[2]) == 2*(int(str(i)[1])):
            cnt += 1

    result = cnt + 99

print(result)