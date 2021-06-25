import sys
input = sys.stdin.readline
'''
find_set으로 하면 통과, find_set2으로 하면 시간초과
전자는 부모를 찾으면서 p 리스트의 정보를 바꿔주는데
후자는 아니라서 그런가...?
'''
def find_set(x):
    if p[x] == x:
        return x
    p[x] = find_set(p[x])
    return p[x]

def find_set2(x):
    if p[x] == x:
        return x
    return find_set2(p[x])

# union
def union(x, y):
    px, py = find_set(x), find_set(y)
    if px != py:
        p[py] = px
    return

N, M = map(int, input().split())
p = list(range(N+1))
for _ in range(M):
    ops, a, b = map(int, input().split())
    if ops:
        print('YES') if find_set(a) == find_set(b) else print('NO')
    else:
        union(a, b)
print(p)