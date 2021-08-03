def solution(n, stations, w):
    # 기지국이 설치되지 않은 구간의 길이
    btw_station = []
    for i in range(1, len(stations)):
        dis = stations[i] - stations[i - 1] - 2 * w - 1
        if dis > 0: btw_station.append(dis)
    first, last = stations[0] - w - 1, n - stations[-1] - w
    if first > 0:
        btw_station.append(first)
    if last > 0:
        btw_station.append(last)

    answer = 0
    for b in btw_station:
        if b % (2 * w + 1):
            answer += 1
        answer += b // (2 * w + 1)

    return answer