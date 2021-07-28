# 사이클 생성 여부: 연결하고자 하는 두 노드의 루트노드가 같으면 생성됨
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def find_set(x):
    if x == p[x]:
        return x
    p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    px = find_set(x)
    py = find_set(y)
    if px < py:
        p[py] = px
    else:
        p[px] = py

N, M = map(int, (input().split()))
p = [i for i in range(N)]
for i in range(M):
    s, e = map(int, input().split())
    if find_set(s) == find_set(e):
        print(i+1)
        break
    union(s, e)
else:
    print(0)