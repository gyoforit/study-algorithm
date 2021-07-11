def solution(lines):
    answer = 0
    timeline = []
    for line in lines:
        tmp = line.split()
        end_times = tmp[1].split(':')
        # ms 단위로 변환
        end_time = int(end_times[0])*3600000+int(end_times[1])*60000+int(end_times[2].replace('.',''))

        T = int(float(tmp[2][:-1])*1000)
        start_time = end_time - T + 1
        if start_time > 0:
            timeline.append((start_time, end_time))
        else:
            timeline.append((0, end_time))
    for i in range(len(timeline)):
        # 현재 확인하는 로그는 무조건 포함이므로 1부터 시작
        cnt = 1
        target_end = timeline[i][1]
        for j in range(len(timeline)):
            if i == j:
                continue
            tmp_start = timeline[j][0]
            tmp_end = timeline[j][1]
            # 현재 확인하고자 하는 로그의 종료시간 부터 1초간 확인
            # 해당 시간대에 시작 시간이 포함
            if target_end <= tmp_start < target_end + 1000:
                cnt += 1
            # 해당 시간대에 종료 시간이 포함
            elif target_end <= tmp_end < target_end + 1000:
                cnt += 1
            # 해당 시간대에 이미 처리 진행중
            elif tmp_start <= target_end and tmp_end >= target_end + 1000:
                cnt += 1
        answer = max(answer, cnt)
    return answer