import sys
sys.stdin = open('input.txt')

def find_coparent(x, y):
    px = [x]
    py = [y]
    now_x = tree[x]
    now_y = tree[y]
    while now_x != tree[now_x]:
        px.append(now_x)
        now_x = tree[now_x]
    while now_y != tree[now_y]:
        py.append(now_y)
        now_y = tree[now_y]
    return px, py

T = int(input())
for _ in range(T):
    N = int(input())
    tree = [0]*(N+1)
    for _ in range(N-1):
        p, k = map(int, input().split())
        tree[k] = p
    a, b = map(int, input().split())
    pa, pb = find_coparent(a, b)
    axb = list(set(pa)&set(pb))
    min_idx = 987654321
    answer = 0
    for i in axb:
        tmp = pa.index(i)
        if tmp < min_idx:
            min_idx = tmp
            answer = i
    print(answer)