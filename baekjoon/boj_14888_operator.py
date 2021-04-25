'''
나눗셈 처리에 유의하기
x = -6, y = 5일 때
int(x/y) = -1
int(x//y) = -2
'''
operators = {0: (lambda x, y: x+y),
             1: (lambda x, y: x-y),
             2: (lambda x, y: x*y),
             3: (lambda x, y: int(x/y))}

def calc(lv, total):
    global mn, mx
    if lv == N-1:
        mn = min(mn, total)
        mx = max(mx, total)
        return

    for i in range(4):
        if opers[i] > 0:
            opers[i] -= 1
            tmp = operators.get(i)(total, nums[lv+1])
            calc(lv+1, tmp)
            opers[i] += 1

N = int(input())
nums = list(map(int, input().split()))
opers = list(map(int, input().split()))
mn = 10**10
mx = -10**10
calc(0, nums[0])
print(mx, mn, sep='\n')