def solution(s):
    answer = []
    cnt = [0] * 100001
    nums = list(map(int, ''.join(''.join(s.split('{')).split('}')).split(',')))
    for i in nums:
        cnt[i] += 1
    while max(cnt) > 0:
        mx = cnt.index(max(cnt))
        answer.append(mx)
        cnt[mx] = 0
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))