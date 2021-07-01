import sys
from collections import deque
input = sys.stdin.readline

def spring():
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            tree_list = deque()
            tree_list += trees[r][c]
            if tree_list:
                idx = len(tree_list)-1
                # print(tree_list)
                while nutri[r][c] > 0 and idx >= 0:
                    # print(tree_list)
                    # print(idx)
                    if nutri[r][c] >= tree_list[idx]:
                        nutri[r][c] -= tree_list[idx]
                        tree_list[idx] += 1
                        idx -= 1
                    else:
                        # print(nutri[r][c], idx)
                        for _ in range(idx):
                            dead_trees[r][c] += tree_list[0] // 2
                            tree_list.popleft()
                        break
            trees[r][c] = tree_list
    return


def summer():
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            nutri[r][c] += dead_trees[r][c]
            dead_trees[r][c] = 0

    return


drc = [(-1, -1), (-1, 0), (-1, 1), (1, -1), (0, -1), (0, 1), (1, 0), (1, 1)]


def fall():
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if trees[r][c]:
                for tree in trees[r][c]:
                    if not (tree % 5):
                        for dr, dc in drc:
                            nr, nc = r + dr, c + dc
                            if 1 <= nr < N + 1 and 1 <= nc < N + 1:
                                trees[nr][nc].append(1)
    return


def winter():
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            nutri[r][c] += A[r][c]
    return


N, M, K = map(int, input().split())
A = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
trees = [[list() for _ in range(N + 1)] for _ in range(N + 1)]
dead_trees = [[0] * (N + 1) for _ in range(N + 1)]
nutri = [[5] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    r, c, age = map(int, input().split())
    trees[r][c].append(age)

for r in range(1, N + 1):
    for c in range(1, N + 1):
        trees[r][c].sort(reverse=True)

for _ in range(K):
    spring()
    summer()
    fall()
    winter()
    # print(trees)

cnt = 0
for r in range(1, N + 1):
    for c in range(1, N + 1):
        if trees[r][c]:
            cnt += len(trees[r][c])
print(cnt)