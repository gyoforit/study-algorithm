# 210201
# 3431. 준환이의 운동관리
T = int(input())
for i in range(T):
    numbers = list(map(int, input().split())) #[300, 400, 240]
    if numbers[0] <= numbers[2] <= numbers[1]:
        zero = 0
        print(f'#{i+1} {zero}')
    elif numbers[2] < numbers[0]:
        todo = numbers[0] - numbers[2]
        print(f'#{i+1} {todo}')
    elif numbers[1] < numbers[2]:
        result = -1
        print(f'#{i+1} {result}')
    
# 8번째 줄 거꾸로 써서 세번이나 틀림... 제대로 보자 ㅠ
'''
< logic >
1. 주어진 input 만큼 for문 돌면서(T번 반복)
2. 3개의 정수를 공백 기준으로 받아서 int로 변환하여 리스트화 함
3. 주어진 조건에 따라 print할 값을 다르게 설정
'''

# 4406. 모음이 보이지 않는 사람
T = int(input())
vowel = 'aeiou'
for i in range(1, T+1):
    chars = []
    chars.extend(input()) # [c, o, n, ...]
    new_chars = []
    for c in chars:
        if c in vowel:
            new_chars.append('')
        else:
            new_chars.append(c)
    result = ''.join(new_chars)
    print(f'#{i} {result}')

'''
< logic >
1. 미리 모음을 vowel에 담아둠
2. T만큼 for문 돌면서
3. extend 사용하여 들어오는 문자열을 철자 하나하나씩 리스트에 담음
4. new_chars 초기화
5. 철자 하나하나 확인하며, 만약 모음이라면 new_chars에 공백을 추가
6. 그렇지 않다면(자음이라면) 원래 철자를 추가
7. new_chars에서 join 사용하여 문자열로 반환
'''

# 10505. 소득 불균형
T = int(input())
for i in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    avg = sum(numbers)/len(numbers)
    result = 0
    for j in range(N):
        if numbers[j] <= avg:
            result += 1
    print(f'#{i} {result}')

'''
< logic >
1. input 받는게 좀 까다로웠음!
2. 테스트케이스 T번만큼 반복하면서
3. 그 안에서 N을 또 input으로 받음
4. numbers들을 공백 기준으로 받아서 int 변환하여 리스트로 만듦
5. 평균 소득 구함
6. print 할 result 초기화
7. 개수가 N개이므로 N을 사용하여 list를 돌면서
8. 평균 이하인 숫자라면 result에 1 더하고 result 반환
'''

# 3314. 보충학습과 평균
T = int(input())
for i in range(1, T+1):
    scores = list(map(int, input().split()))
    new_scores = []
    for score in scores:
        if score < 40:
            new_scores.append(40)
        else:
            new_scores.append(score)
    avg = int(sum(new_scores)/len(new_scores))
    print(f'#{i} {avg}')

'''
< logic >
1. T만큼 반복하면서 scores에 숫자를 리스트로 담음
2. new_scores 초기화
3. scores의 점수 하나하나 돌면서
4. 만약 score가 40 미만이면 40을 append
5. 그렇지 않으면 원래 점수 append
6. 평균 내서 반환
'''

# 210203
# 1213. [S/W 문제해결 기본] 3일차 - String
for i in range(1, 11):
    N = input()
    chars = ''
    sentence = ''
    result = 0
    chars += input()
    sentence += input()
    for j in range(len(sentence)):
        if sentence[j:j+len(chars)] == chars:
            result += 1
    print(f"#{i} {result}")

'''
< logic >
1. input 처리를 좀 고민해봤음
2. 우선 테스트케이스가 10개이므로 for문으로 10번 반복
3. 첫번째 input은 N에 저장(별로 쓸데 없음)
4. 두번째 input은 문자열이므로 빈 문자열 chars에 저장
5. 세번째 input은 문장이므로 빈 문자열 sentence에 저장
6. 겹치는 횟수 셀 result 초기화
7. 문장의 첫글자부터 시작하여 chars의 길이만큼 slicing
8. 만약 슬라이싱한게 chars와 일치한다면 result에 1 카운트
9. result를 반환!
* 처음엔 리스트 extend 하려고 했으나, 굳이 그럴 필요 없는듯. 오히려 더 복잡해짐.
'''

