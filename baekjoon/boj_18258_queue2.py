import sys
sys.stdin = open('input.txt')
from collections import deque

T = int(input())
queue = deque()
for _ in range(T):
    order = input().split()
    if order[0] == 'push':
        queue.append(int(order[1]))
    elif order[0] == 'pop':
        tmp = -1 if not queue else queue.popleft()
        print(tmp)
    elif order[0] == 'size':
        print(len(queue))
    elif order[0] == 'empty':
        tmp = 0 if queue else 1
        print(tmp)
    elif order[0] == 'front':
        tmp = -1 if not queue else queue[0]
        print(tmp)
    else:
        tmp = -1 if not queue else queue[-1]
        print(tmp)