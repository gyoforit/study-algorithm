import sys
sys.stdin = open('input.txt')
N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()
l, r = 1, trees[-1]
answer = 0
while l <= r:
    mid = (l+r)//2
    cnt = 0
    for tree in trees:
        tmp = tree-mid
        if tmp>0: cnt += tmp
    if cnt >= M:
        l = mid+1
    else:
        r = mid-1
print(r)
