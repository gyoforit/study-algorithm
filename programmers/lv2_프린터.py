from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque()
    priorities = [(idx, priority) for idx, priority in enumerate(priorities)]
    while priorities:
        tmp = priorities[1:]
        for idx, p in priorities:
            if p > priorities[0][1]:
                target = priorities.pop(0)
                priorities.append(target)
                break
        else:
            if priorities[0][0] == location:
                return len(queue)+1
            target = priorities.pop(0)
            queue.append(target)