# itertools의 permutaions 이용해도 되지만 DFS 이용해서 풀어보았음
# nums.remove(i)를 쓰면 index error가 나는데 왜지?

def dfs(lv):
    global check, nums
    if lv == M and check.count(1) == M:
        print(*nums)
        return

    for i in range(1, N+1):
        if not check[i]:
            check[i] = 1
            nums.append(i)
            dfs(lv+1)
            nums.pop()
            check[i] = 0

N, M = map(int, input().split())
check = [0]*(N+1)
nums = []
dfs(0)
