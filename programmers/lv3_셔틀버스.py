def solution(n, t, m, timetable):
    timetable_2 = []
    for time in timetable:
        time = int(time[:2]) * 60 + int(time[3:])
        timetable_2.append(time)
    timetable_2.sort()
    # 버스 탄 인원 세는용
    cnt = 0
    # 버스 출발 시각 (9:00부터 시작)
    now = 540
    # n번째 버스에 몇명탔는지 저장용
    bus = [0]
    bus_num = 1
    # i번째 크루(탑승하려는 크루의 순서)
    i = 0
    # 종료조건
    # 1. 모든 크루가 다 탑승한다
    # 2. 마지막 버스까지 다 떠난다
    print(timetable_2)
    print(now)
    while True:
        # 현재 대기중인 버스보다 일찍 도착했다면 탑승
        if timetable_2[i] <= now:
            cnt += 1
            i += 1
            # 버스 만석이라면 보내기
            if cnt == m:
                bus.append(cnt)
                cnt = 0
                now += t
                bus_num += 1
        # 가장 일찍 온 사람 조차 이번 버스 못 탄다면 그냥 보내기
        else:
            bus.append(cnt)
            cnt = 0
            bus_num += 1
            now += t
        # 막차까지 보냈을 때 or 마지막 크루까지 다 태웠을 때
        if bus_num == n+1 or i == len(timetable_2):
            break

    print(bus)
    print(i)
    print(now)
    # case1: 막차에 정원보다 적게 탄 경우 -> 막차에 탄다.
    if bus[-1] < m:
        print('막차에 정원보다 적게 탄 경우')
        print(540+(n-1)*t)
        answer = str((540+(n-1)*t)//60).zfill(2)+':'+str((540+(n-1)*t)%60).zfill(2)
    # case2: 막차가 정원인 경우 -> 마지막에서 -m 번째 사람보다 1분 빨리 선다.
    else:
        print('막차가 정원인 경우')
        last = timetable_2[-m]
        print('막차의 첫 손님: ', last)
        print(timetable_2[-m:].count(last))
        if timetable_2[-m:].count(last) < m:
            answer = str(last//60).zfill(2) + ':' + str(last%60).zfill(2)
        else:
            answer = str((last-1)//60).zfill(2) + ':' + str((last-1)%60).zfill(2)
    return answer

print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(1, 1, 1, ["23:59"]))
print(solution(10, 60, 45, ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))