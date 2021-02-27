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