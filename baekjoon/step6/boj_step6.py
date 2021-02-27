# 백준 6단계 - 함수
# 210227
# 15596. 정수 N개의 합
def solve(a):
    ans = 0
    for i in a:
        ans += i
    return ans

# 1065. 한수
def sol(N):
    ans = []
    for i in range(1, N+1):
        tmp = i
        tmplist = []
        while tmp > 0:
            tmplist.append(tmp % 10)
            tmp = tmp // 10
        if len(tmplist) <= 2:
            ans.append(i)
        else:
            x = tmplist[0] - tmplist[1]
            for j in range(len(tmplist)-1):
                if tmplist[j] - tmplist[j+1] != x:
                    break
            else:
                ans.append(i)
    return len(ans)

N = int(input())
print(sol(N))

# map활용하는 법도 있음! string으로 변환
N = int(input())
for n in range(1, N+1):
    # 99까진 생략
    nums = list(map(int, str(n))) # 자릿수대로 끊어짐!!

# 4673. 셀프 넘버
d_list = []
# 셀프 넘버가 아닌 수들을 append하는 함수 (재귀 사용)
def d(N):
    if N > 10000:
        return
    else:
        result = N
        N_list = list(map(int, str(result)))
        result += sum(N_list)
        if result <= 10000:
            d_list.append(result)
        return d(result)

# d 함수 사용해서 셀프 넘버가 아닌 수들을 모두 append
for i in range(1, 10001):
    if i not in d_list:
        d(i)

# d_list에 없는 수들만 print
for j in range(1, 10001):
    if j not in d_list:
        print(j)