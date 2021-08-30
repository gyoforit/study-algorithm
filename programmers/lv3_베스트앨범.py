# 장르: [(고유번호, 재생량), (고유번호, 재생량)] 형식으로 딕셔너리에 저장
# 재생수 총합을 기준으로 정렬한 후, 그 안에서 재생량 내림-고유번호 오름차순으로 정렬
def solution(genres, plays):
    genre_dict = dict()
    for i in range(len(genres)):
        if not genre_dict.get(genres[i]):
            genre_dict[genres[i]] = [(i, plays[i])]
        else:
            genre_dict[genres[i]].append((i, plays[i]))
    totals = sorted(list(genre_dict.items()), key=lambda x: sum([i[1] for i in x[1]]), reverse=True)
    answer = []
    for total in totals:
        tmp = sorted(total[1], key=lambda x: (-x[1], x[0]))
        if len(tmp) >= 1:
            answer.append(tmp[0][0])
        if len(tmp) >= 2:
            answer.append(tmp[1][0])
    return answer