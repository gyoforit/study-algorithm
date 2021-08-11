import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
N = int(input())
points = []
for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

points.sort(key=lambda x: (x[0], x[1]))
for point in points:
    print(*point)