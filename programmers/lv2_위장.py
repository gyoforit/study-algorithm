def solution(clothes):
    category = dict()
    for name, kind in clothes:
        if category.get(kind):
            category[kind] += 1
        else:
            category[kind] = 1
    answer = 1
    for cate in category.values():
        answer *= (cate+1)
    return answer-1