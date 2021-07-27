# set 사용해서 중복 체크
# 사람: 인덱스+1 을 n으로 나눈 나머지 (0이면 n)
# 차례: 인덱스를 n으로 나눈 몫+1
# for-else 문: for문을 break 없이 끝까지 돌면 else문 탐
def solution(n, words):
    answer = []
    already = set()
    before = words[0]
    already.add(before)
    for i in range(1, len(words)):
        now = words[i]
        if now not in already and before[-1] == now[0]:
            already.add(now)
            before = now
        else:
            person = (i+1)%n if (i+1)%n else n
            answer.append(person)
            answer.append((i//n)+1)
            break
    else:
        answer = [0, 0]
    return answer