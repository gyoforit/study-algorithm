import sys
input = sys.stdin.readline
def join(time):
    hour, minute = int(time[:2]), int(time[-2:])
    start_h, start_m = int(S[:2]), int(S[-2:])
    if hour < start_h:
        return True
    elif hour == start_h and minute <= start_m:
        return True
    return False

def out(time):
    hour, minute = int(time[:2]), int(time[-2:])
    end_h, end_m = int(E[:2]), int(E[-2:])
    sming_h, sming_m = int(Q[:2]), int(Q[-2:])
    flag = 0
    if hour > end_h:
        flag = 1
    elif hour == end_h and minute >= end_m:
        flag = 1

    if not flag:
        return False
    else:
        if hour < sming_h:
            return True
        elif hour == sming_h and minute <= sming_m:
            return True
    return False

S, E, Q = input().split()
members = dict()
while True:
    try:
        t, id = input().split()
        if join(t):
            if id not in members.keys():
                members[id] = [1, 0]
            else:
                if members[id][0] == 0:
                    members[id][0] += 1
        elif out(t):
            if id not in members.keys():
                members[id] = [0, 1]
            else:
                if members[id][1] == 0:
                    members[id][1] += 1
        # print(t, id, members)
    except:
        break

print(list(members.values()).count([1, 1]))

'''
시간을 단순히 네자리수로 표현하면 크기비교만 하면 됨
ex. 22:00 -> 2200
입장/퇴장을 각각 set으로 만들어서 교집합연산인 & 해주면 됨
'''
import sys

S, E, Q = sys.stdin.readline().split()
S = int(''.join(S.replace(':', '')))
E = int(''.join(E.replace(':', '')))
Q = int(''.join(Q.replace(':', '')))
enter = set()
out = set()

while True:
    try:
        time, name = sys.stdin.readline().split()
        time = int(''.join(time.replace(':', '')))
        if time <= S:
            enter.add(name)
        elif E <= time <= Q:
            out.add(name)
    except:
        break
print(len(list(enter&out)))