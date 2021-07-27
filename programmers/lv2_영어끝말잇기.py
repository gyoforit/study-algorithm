# set 사용해서 있는지 체크
# 몇번째 사람인지는 인덱스+1 을 n으로 나눈 나머지 (0이면 n)
# 차례는 인덱스를 n으로 나눈 몫+1
def solution(n, words):
    answer = []
    already = set()
    before = words[0]
    already.add(before)
    flag = 0
    for i in range(1, len(words)):
        now = words[i]
        if now not in already and before[-1] == now[0]:
            already.add(now)
            before = now
        else:
            person = (i+1)%n if (i+1)%n else n
            answer.append(person)
            answer.append((i//n)+1)
            flag = 1
            break
    if not flag:
        answer = [0, 0]
    return answer