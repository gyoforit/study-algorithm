import sys
sys.stdin = open('input.txt')

def check(x):
    if parent[x] != x:
        parent[x] = check(parent[x])
    return parent[x]

def union(x, y):
    px = check(x)
    py = check(y)
    if px < py:
        parent[py] = px
    else:
        parent[px] = py
    return

V, E = map(int, input().split())
parent = [i for i in range(V+1)]
AL = []
for _ in range(E):
    s, e, point = map(int, input().split())
    AL.append((s, e, point))
AL.sort(key=lambda x: x[2])
ans = 0
for s, e, point in AL:
    print(s, e)
    print(check(s), check(e))
    if check(s) != check(e):
        ans += point
        union(s, e)
print(ans)
print(parent)