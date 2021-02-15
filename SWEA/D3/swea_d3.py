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

# 210205
# 11387. 몬스터 사냥
T = int(input())
for i in range(1, T+1):
    D, L, N = map(int, input().split())
    total = 0
    for j in range(N):
        total += D*(1+j*L*0.01)
    print(f"#{i} {int(total)}")

# 10912. 외로운 문자
T = int(input())
for i in range(1, T+1):
    chars = []
    result = {}
    answer = []
    chars.extend(input())
    # dict에 {키: 센 횟수}
    for char in chars:
        if char in result.keys():
            result[char] += 1
        else:
            result[char] = 1
    # value가 홀수면 중복되지 않은 하나 있는거니까 list에 append
    for key in result.keys():
        if result[key] % 2:
            answer.append(key)

    if answer == []:
        print(f"#{i} Good")
    else:
        answer.sort()
        print(f"#{i} {''.join(answer)}")

# 영주님 풀이
for t in range(1, int(input())+1):
    sentence = input()
    result = ''
    for digit in sentence:
        count = sentence.count(digit)
        if (count == 1) or ((count % 2) and (digit not in result)):
            result += digit
    
    if result:
        sorted_result = ''.join(sorted(list(result)))
        print(f'#{t} {sorted_result}')
    else:
        print(f'#{t} Good')

# 호근님 풀이
T = int(input())
for test_case in range(1, T + 1):
    check = set()
    word = input()
    for ch in word:
        if ch in check:
            check.remove(ch)
        else:
            check.add(ch)
    print('#{} {}'.format(test_case, 'Good' if len(check) == 0 else ''.join(sorted(check))))

# 210207
# 5431. 민석이의 과제 체크하기
'''
< logic >
1. 1~N 있는 리스트 students 생성
2. 제출한 학생들을 리스트로 받아서 하나씩 students에서 제거
(remove 써도 되는 이유? 중복되는 번호 없다고 했으니까)
3. 남은 students 요소들을 print
'''
T = int(input())
for i in range(1, T+1):
    N, K = map(int, input().split())
    students = []
    for num in range(1, N+1):
        students.append(str(num))
    submit = list(map(int, input().split()))
    for n in submit:
        students.remove(str(n))
    print(f"#{i} {' '.join(students)}")

# 5549. 홀수일까 짝수일까
T = int(input())
for i in range(1, T+1):
    if int(input()) % 2:
        print(f"#{i} Odd")
    else:
        print(f"#{i} Even")

# 9700. USB 꽂기의 미스테리
'''
p의 확률로 올바른 면으로 꽂음 / (1-p) 로 뒤집어서
올바른 면으로 꽂았을 때 -> q의 확률로 정상적으로 꽂힘
뒤집어서 꽂았을 때 -> 100% 안 꽂힘
s1: 한번 뒤집었을 때 usb가 꽂힐 확률 / 처음에 거꾸로. (1-p)*q
s2: 두번 뒤집었을 때 꽂힐 확률 / 올바르게but실패->거꾸로->올바르게 / p*(1-q)*q
< 중요한 것 > 뒤집어서 낄 때 확률은 안 곱해도 됨! 왜냐 100% 뒤집어서 끼니까
'''
T = int(input())
for i in range(1, T+1):
    p, q = map(float, input().split())
    if (1-p)*q < p*(1-q)*q:
        print(f"#{i} YES")
    else:
        print(f"#{i} NO")

# 210208
# 1206. [S/W 문제해결 기본] 1일차 - View
'''
알아보고자 하는 건물을 i라고 가정
i-1, i-2(왼쪽) i+1, i+2(오른쪽)
각 방향당 i와의 차이가 둘다 0보다 크다 -> 조망권이 있다
최솟값을 구해서 더함
'''
T = int(input())
for t in range(1, T+1):
    N = int(input())
    buildings = list(map(int, input().split()))
    count = 0
    for i in range(2, len(buildings)-2):
        mn1 = 0
        mn2 = 0
        a = buildings[i] - buildings[i-1]
        b = buildings[i] - buildings[i-2]
        if a > 0 and b > 0:
            if a < b:
                mn1 = a
            else:
                mn1 = b
        c = buildings[i] - buildings[i+1]
        d = buildings[i] - buildings[i+2]
        if c > 0 and d > 0:
            if c < d:
                mn2 = c
            else:
                mn2 = d
        if mn1 < mn2:
            count += mn1
        else:
            count += mn2
    print(count)

# 210209
# 1208. [S/W 문제해결 기본] 1일차 - Flatten
for t in range(1, 11):
    N = int(input())
    box = list(map(int, input().split()))
    # 최대, 최소의 index를 0번째로 초기화
    mx = 0
    mn = 0
    # 첫 리스트에서 최대, 최소의 index 설정
    for idx in range(100):
        if box[idx] > box[mx]:
            mx = idx
        elif box[idx] < box[mn]:
            mn = idx

    for i in range(1, N+1): # 덤프 횟수
        box[mx] -= 1
        box[mn] += 1
        for idx in range(100):
            if box[idx] > box[mx]:
                mx = idx
            elif box[idx] < box[mn]:
                mn = idx

    print('#%d %d' % (t, (box[mx] - box[mn])))

# 5789. 현주의 상자 바꾸기
'''
1부터 N번까지의 상자.
Q회 동안 숫자 변경할거임
범위는 L번부터 R번까지 i(1<=i<=Q)로 변경
'''
T = int(input())
for t in range(1, T+1):
    N, Q = map(int, input().split())
    result = ''
    box = [0] * N
    for q in range(1, Q+1): # Q개의 작업
        L, R = map(int, input().split()) #인덱스로 따지면 L-1 ~ R-1
        for a in range(L-1, R):
            box[a] = q
    for i in range(len(box)):
        box[i] = str(box[i])
    result = ' '.join(box)
    print('#%d %s' % (t, result))

# 210210
# 6485. 삼성시의 버스 노선
T = int(input())
for t in range(1, T+1):
    busstop = [0] * 5001 # 인덱스가 곧 정류장 번호이므로 편의상 5001로! (0~5000)
    result = []
    N = int(input())
    for n in range(1, N+1):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            busstop[i] += 1
    P = int(input())
    for p in range(1, P+1):
        C = int(input())
        result += [busstop[C]]

    # 원래 했던거.. 일일이 str로 바꾸기 ㅠ
    # for i in range(len(result)):
    #     result[i] = str(result[i])
    # result = ' '.join(result)
    
    # 새로 배운거!! 정수 리스트를 [] 떼고 문자열로 출력하는 법
    result = ' '.join([str(x) for x in result])
    # result = ' '.join(map(str, result))
    print('#%d %s' % (t, result))

# 210211
# 1289. 원재의 메모리 복구하기
'''
처음부터 하나씩 돌면서 0으로 초기화한 now와 다른 숫자면 count +1 해주고 now를 해당 숫자로 바꿈
숫자가 달라질때마다 count가 올라가게!
'''
T = int(input())
for t in range(1, T+1):
    N = input()
    cnt = 0
    now = 0
    for n in N: # 한글자씩 확인하면서
        if int(n) != now:
            cnt += 1
            now = int(n)
    print("#%d %d" % (t, cnt))

# 5601. [Professional] 쥬스 나누기
'''
이건...뭐지 독해 문제인가
'''
T = int(input())
for t in range(1, T+1):
    N = input()

    print("#%d" % t, end=' ')
    for n in range(int(N)):
        print("1/%s" % N, end= ' ')
    print()

# 10570. 제곱 팰린드롬 수
'''
오래 걸렸던 문제... 알고리즘 노트 참고!
'''
import math
def ispalindrome(n):
    if len(str(n)) == 0:
        return True
    if type(n) == float:
        if n.is_integer() == False:
            return False
        else:
            return ispalindrome(int(n))
    else:
        N = str(int(n))
        cnt = 0
        for _ in N:
            cnt += 1

        if cnt <= 1:
            return True
        if N[0] == N[-1]:
            return ispalindrome(N[1:-1])
        else:
            return False

T = int(input())
for t in range(1, T + 1):
    A, B = map(int, input().split())
    cnt = 0
    for a in range(A, B + 1):
        if ispalindrome(a) == True and ispalindrome(a ** 0.5) == True:
            cnt += 1
    print(cnt)

# 다른 풀이
def check(num):
    num = str(num)
    for i in range(len(num) // 2):
        if num[i] != num[-1 - i]:
            return False
    else:
        return True

for T in range(1, int(input()) + 1):
    A, B = map(int, input().split())
    cnt = 0
    for i in range(A, B + 1):
        if i ** 0.5 == int(i ** 0.5) and check(i) and check(int(i ** 0.5)):
            cnt += 1
    print('#{} {}'.format(T, cnt))

# 활용해서 다시 제출
def ispalindrome(n):
    N = str(n)
    cnt = 0
    for _ in N:
        cnt += 1
    if cnt <= 1:
        return True
    if N[0] == N[-1]:
        return ispalindrome(N[1:-1])
    else:
        return False

T = int(input())
for t in range(1, T + 1):
    A, B = map(int, input().split())
    cnt = 0
    for a in range(A, B + 1):
        if a ** 0.5 == int(a ** 0.5) and ispalindrome(a) == True and ispalindrome(int(a ** 0.5)) == True:
            cnt += 1
    print("#%d %d" % (t, cnt))

# 210212
# 3456. 직사각형 길이 찾기
# 왜 테케 절반정도만 맞지...?
T = int(input())
for t in range(1, T+1):
    nums = list(map(int, input().split()))
    half_sum = nums[0]
    total = 0
    for n in range(3):
        if nums[n] != nums[0]:
            half_sum += nums[n]
        total += nums[n]

    if half_sum == nums[0]:
        print("#%d %d" % (t, nums[0]))
    else:
        print("#%d %d" % (t, (half_sum*2-total)))
        
# pass한 답
T = int(input())
for t in range(1, T+1):
    nums = list(map(int, input().split()))
    cnt = [0] * 101
    for i in nums:
        cnt[i] += 1

    if 3 in cnt:
        print("#%d %d" % (t, nums[0]))
    else:
        for i in range(101):
            if cnt[i] == 1:
                print("#%d %d" % (t, i))

# 210215
# 1209. [S/W 문제해결 기본] 2일차 - Sum
for t in range (1, 11):
    T = int(input())
    arr = []
    for i in range(100):
        arr.append(list(map(int, input().split())))
    mx = 0
    a = len(arr)
    # 각 행의 합
    for i in range(a):
        total_1 = 0
        for j in range(a):
            total_1 += arr[i][j]
        if total_1 > mx:
            mx = total_1
    # 각 열의 합
    for j in range(a):
        total_2 = 0
        for i in range(a):
            total_2 += arr[i][j]
        if total_2 > mx:
            mx = total_2
    for i in range(a):
        total_3 = 0
        total_3 += arr[i][i]
    if total_3 > mx:
        mx = total_3
    for i in range(a):
        total_4 = 0
        total_4 += arr[a-1-i][i]
    if total_4 > mx:
        mx = total_4
    print("#%d %d" % (T, mx))