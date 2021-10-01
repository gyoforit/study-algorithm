import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

deque = []
T = int(input())
for _ in range(T):
    order = input().split()
    if len(order) == 2:
        if order[0] == 'push_back':
            deque.append(int(order[1]))
        else:
            deque = [int(order[1])] + deque
    else:
        if order[0] == 'pop_front':
            target = -1 if not deque else deque.pop(0)
            print(target)
        elif order[0] == 'pop_back':
            target = -1 if not deque else deque.pop(-1)
            print(target)
        elif order[0] == 'size':
            print(len(deque))
        elif order[0] == 'empty':
            print(0) if deque else print(1)
        elif order[0] == 'front':
            print(-1) if not deque else print(deque[0])
        else:
            print(-1) if not deque else print(deque[-1])