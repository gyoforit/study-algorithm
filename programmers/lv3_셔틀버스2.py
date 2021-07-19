from collections import Counter
def solution(n, t, m, timetable):
    timetable_2 = []
    for time in timetable:
        time = int(time[:2]) * 60 + int(time[3:])
        timetable_2.append(time)
    time_dict = Counter(timetable_2)
    timeline = sorted(list(time_dict.keys()))
    print(time_dict)
    now = 540
    cnt = 0
    bus_num = 1
    bus = [0]
    for i in range(len(timeline)):
        print(timeline[i], cnt, bus)
        if timeline[i] <= now:
            crews = time_dict[timeline[i]]
            if cnt+crews < m:
                cnt += crews
            else:
                bus.append(m)
                remain = crews-m+cnt
                cnt = remain
                bus_num += 1
                now += t
        else:
            bus.append(cnt)
            cnt = 0
            bus_num += 1
            now += t
        if bus_num == n+1:
            break
        if i == len(timeline)-1:
            bus.append(cnt)
    print(bus)



print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(1, 1, 1, ["23:59"]))
print(solution(10, 60, 45, ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))