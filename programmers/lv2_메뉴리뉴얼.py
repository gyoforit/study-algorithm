from itertools import combinations
def solution(orders, course):
    menu_dict = dict()
    # 메뉴구성개수를 key로 둔 dict 생성
    for cour in course:
        menu_dict[cour] = dict()
    # 주문별 조합을 만든 후, dict 안에 있는 길이만 dict에 넣기
    for order in orders:
        L = len(order)
        for i in range(2, L + 1):
            combs = list(combinations(order, i))
            for comb in combs:
                tmp = ''.join(sorted(list(comb)))
                if len(tmp) in menu_dict.keys():
                    if menu_dict[len(tmp)].get(tmp):
                        menu_dict[len(tmp)][tmp] += 1
                    else:
                        menu_dict[len(tmp)][tmp] = 1

    # 최댓값이면서 2번 이상 주문된 것만 answer에 append
    answer = []
    for value in menu_dict.values():
        tmp_list = sorted(list(value.items()), key=lambda x: -x[1])
        if tmp_list:
            mx = tmp_list[0][1]
            for tm in tmp_list:
                if tm[1] == mx and mx >= 2:
                    answer.append(tm[0])
                else:
                    break
    answer.sort()

    return answer