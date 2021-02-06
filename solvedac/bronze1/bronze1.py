# 210206
# 1032. 명령프롬프트
'''
< logic >
1. 첫번째 문자를 리스트에 넣음
2. 다음 문자들과 비교해서 같으면 냅두고 다르면 물음표로 변경
'''
# 1차 시도: 틀림
T = int(input())
first = []
first.extend(input())
for i in range(1, T):
    filename = input()
    for j in range(len(filename)):
        if filename[j] != first[j]:
            first.remove(first[j])
            first.insert(j, "?")
print(''.join(first))
# 처음 답이 틀린이유: remove는 처음 값만 지우기 때문!
# 이 표현대로 하려면 del list[index]로 해야됨!

# 2차 시도: 맞음
T = int(input())
first = []
first.extend(input())
for i in range(1, T):
    filename = input()
    for j in range(len(filename)):
        if filename[j] != first[j]:
            first[j] = "?"
print(''.join(first))
# 리스트는 단순히 값을 재 할당하는 것만으로 변경이 가능하다!

# 영주님 풀이 - zip 이용...천재신가
n = int(input())
texts = []
for _ in range(n):
    texts.append(input())
​
columns = list(zip(*texts))
result = ''
for column in columns:
    if column.count(column[0]) < n:
        result += '?'
    else:
        result += column[0]
print(result)