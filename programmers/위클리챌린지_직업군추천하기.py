def solution(table, languages, preference):
    result = []
    for t in table:
        t = t.split()
        cnt = 0
        for i in range(len(languages)):
            idx = 6-t.index(languages[i]) if languages[i] in t else 0
            cnt += preference[i]*idx
        result.append((t[0], cnt))
    print(result)
    mx = max([r[1] for r in result])
    answer = sorted([(job, score) for job, score in result if score==mx], key=lambda x: x[0])[0][0]
    return answer