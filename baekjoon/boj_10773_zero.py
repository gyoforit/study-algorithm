# import sys 쓰니까 시간이 거의 1/40 으로 줄었다
# 앞으로는 써버릇하기!
import sys
input = sys.stdin.readline
N = int(input())
stack = []
for _ in range(N):
    target = int(input())
    if target:
        stack.append(target)
    else:
        stack.pop()

print(sum(stack))