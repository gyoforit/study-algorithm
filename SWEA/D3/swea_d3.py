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
# 210223 - 4406 수정
vowel = 'aeiou'
T = int(input())
for t in range(1, T+1):
    chars = []
    chars.extend(input())
    new_chars = []
    for c in chars:
        # vowel에 없을 때만 새 리스트에 append
        if c not in vowel:
            new_chars.append(c)
    result = ''.join(new_chars)
    print("#%d %s" % (t, result))

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
# 왜 테케 절반정도만 맞지...? 오류 찾음!
T = int(input())
for t in range(1, T+1):
    nums = list(map(int, input().split()))
    half_sum = nums[0]
    total = 0
    for n in range(3):
        if nums[n] != nums[0]: # 이부분이 오류다. 다른 값을 한번 찾고 바로 종료해야 됨!
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

# 210217
# 1221. GNS
GNS = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
T = int(input())
for t in range(1, T+1):
    N = input()
    # 긴 문자열을 공백 단위로 끊어서 리스트에 담기
    num = list(map(str, input().split()))
    # 각 문자당 등장 횟수를 세기 위한 cnt 리스트 준비
    # GNS와 cnt의 인덱스를 똑같게 매칭할 것임 0 = ZRO, 1 = ONE ...
    cnt = [0]*10
    # 문자열 리스트의 요소를 하나씩 꺼내서
    for n in num:
        # GNS 리스트의 순서대로 비교하며 그 값이 같으면 GNS의 인덱스와 같은 cnt 인덱스에 +1
        # GNS와 cnt의 인덱스는 의미가 같기 때문에!
        # ex. GNS[0] = 'ZRO', cnt[0] = 'ZRO'가 나온 개수
        for g in range(len(GNS)):
            if n == GNS[g]:
                cnt[g] += 1
                # 시간 아끼기 위해 값 찾으면 break로 빠져나감
                break
    result = ''
    # cnt 리스트 돌면서 값이 있으면(=0이 아니면)
    # GNS에서 같은 인덱스의 값을 cnt[i]번 만큼 곱해서 result에 차곡차곡 더하기
    for i in range(len(cnt)):
        if cnt[i] != 0:
            result += (GNS[i] + ' ')*cnt[i]
    # 맨 끝에 있는 공백 없애기 위해 rstrip()
    result = result.rstrip()
    print("#%d" % t)
    print(result)

# 210218
# 1216. 회문2
# 회문 판별 함수
def ispalin(arr):
    for i in range(len(arr)//2):
        if arr[i] != arr[-i-1]:
            return False
    return True

T = 10
for t in range(1, T+1):
    N = int(input())
    grid1 = []
    # grid1의 전치행렬(열 검사하기 까다로우니까..)
    grid2 = []
    for i in range(100):
        grid1.append(list(input()))
    grid2 = list(zip(*grid1))

    # grid1 검사
    mx = 1
    # 최대길이 구하는거니까 100부터 내려가기
    for l in range(100, 1, -1):
        # 기존 최대길이가 검사할 길이 이상이면 더이상 비교할 필요 x
        if l <= mx:
            break
        for i in range(100-l+1): # 비교할 인덱스 처음 부분
            for g in grid1:
                if ispalin(g[i:i+l]):
                    if l > mx:
                        mx = l
    # grid2 검사
    for l in range(100, 1, -1):
        if l <= mx:
            break
        for i in range(100-l+1):
            for g in grid2:
                if ispalin(g[i:i+l]):
                    if l > mx:
                        mx = l

    print("#%d %d" % (t, mx))

# 210219
# 5356. 의석이의 세로로 말해요
T = int(input())
for t in range(1, T+1):
    l = 0
    str = []
    for i in range(5):
        str.append(input())
        # 리스트 받으면서 최대 길이 측정까지 같이 함
        if len(str[i]) > l:
            l = len(str[i])
    result = ''
    for c in range(l):
        for r in range(5):
            try:
                result += str[r][c]
            # 인덱스 오류 나면 (= 해당 자리에 문자 없으면) 아무것도 x
            except:
                pass

    print("#%d %s" % (t, result))

# 4047. 영준이의 카드 카운팅
T = int(input())
for t in range(1, T+1):
    S = input()
    s = len(S)
    card = []
    i = 0
    # 크기 3씩 슬라이싱해서 card 리스트 만들기
    while i < s:
        card += [S[i:i+3]]
        i += 3
    # 중복 여부 확인
    if len(card) != len(set(card)):
        print("#%d ERROR" % (t))
    else:
        # 모양 별 개수 세기
        cnt = [0]*4
        for c in card:
            if c[0] == 'S':
                cnt[0] += 1
            elif c[0] == 'D':
                cnt[1] += 1
            elif c[0] == 'H':
                cnt[2] += 1
            else:
                cnt[3] += 1
        # 모자란 카드 수 구하기
        result = [0]*4
        for j in range(4):
            result[j] += 13-cnt[j]

        print("#%d %s" % (t, ' '.join(map(str, result))))

# 11315. 오목 판정
# 대각선 체크하는게 대박 힘들었다... 다섯개 셀 수 있는 출발 인덱스 구하기가 핵심
# 큰 for 의 작은 for - break - else 구문에서 else 빼버리면 안됨! break 걸려도 실행되기 때문..
def check_omok(arr):
    # 행 검사
    N = len(arr)
    for r in range(N):
        for c in range(N-4): # 비교 시작점
            for i in range(5):
                if arr[r][c+i] != 'o':
                    break
            else:
                return 'YES'
    # 열 검사
    for c in range(N): # N = 6 일 때를 상상
        for r in range(N-4):
            for i in range(5):
                if arr[r+i][c] != 'o':
                    break
            else:
                return 'YES'

    # 좌상향 대각선
    drc = [[1, 1], [1, -1]]
    for c in range(N-4): # 0, 1
        for r in range(N-4): # 0, 1
            for i in range(5):
                if arr[r+(drc[0][0]*i)][c+(drc[0][1]*i)] != 'o':
                    break
            else:
                return 'YES'

    # 우상향 대각선
    for c in range(N-1, 3, -1): # 5, 4
        for r in range(N-4): # 0, 1
            for i in range(5):
                if arr[r+(drc[1][0]*i)][c+(drc[1][1]*i)] != 'o':
                    break
            else:
                return 'YES'
    return 'NO'

T = int(input())
for t in range(1, T+1):
    N = int(input())
    board = []
    for n in range(N):
        tmp = []
        tmp.extend(input())
        board += [tmp]
    result = check_omok(board)
    print("#%d %s" % (t, result))

# 3499. 퍼펙트 셔플
T = int(input())
for t in range(1, T+1):
    N = int(input())
    card = list(input().split())
    result = []
    # 홀수일 땐 짝이 안 맞으니까 맨 뒤에 공백 추가한 후 N + 1
    if N % 2:
        card += [' ']
        N += 1
    for i in range((N//2)):
        result += [card[i]]
        result += [card[(N//2)+i]]
    # 홀수인 경우 위해 오른쪽 공백 제거
    result = ' '.join(result).rstrip()
    print("#%d %s" % (t, result))

# 210220
# 2805. 농작물 수확하기
# 예외 케이스에 항상 주의하자!!!
T = int(input())
for t in range(1, T+1):
    N = int(input())
    farm = []
    for _ in range(N):
        tmp = []
        tmp.extend(input())
        farm.append(list(map(int, tmp)))
    if N == 1:
        print("#%d %d" % (t, farm[0][0]))
    else:
        c = N//2  # 중심열
        harv = farm[0][c] + farm[N-1][c] # 맨 위, 아래 더하고 시작
        for r in range(1, N-1):
            harv += farm[r][c] # 중심점 더함
            if r <= N//2:
                for i in range(1, r+1):
                    harv += farm[r][c-i] + farm[r][c+i]
            else:
                for i in range(1, N-r):
                    harv += farm[r][c-i] + farm[r][c+i]
        print("#%d %d" % (t, harv))

# 210223
# 1234. [S/W 문제해결 기본] 10일차 - 비밀번호
# D2 4873이랑 원리 똑같은 문제
for t in range(1, 11):
    N, S = input().split()
    stack = []
    for s in S:
        if not stack or stack[-1] != s:
            stack.append(s)
        else:
            stack.pop()
    print("#%d %s" % (t, ''.join(stack)))

# 1217. [S/W 문제해결 기본] 4일차 - 거듭 제곱
def power(n, m):
    if m == 0:
        return 1
    elif m == 1:
        return n
    else:
        return n*power(n, m-1)

for _ in range(1, 11):
    T = int(input())
    N, M = map(int, input().split())
    result = power(N, M)
    print("#%d %d" % (T, result))

# 1215. [S/W 문제해결 기본] 3일차 - 회문1
def ispalin(n, arr):
    l = len(arr)
    cnt = 0
    for r in range(l):
        for c in range(l-n+1):
            tmp = ''
            for i in range(n):
                tmp += arr[r][c+i]
            if tmp == tmp[::-1]:
                cnt += 1
    # 급하게 푸느라 중복 신경 못 씀..나중에 윗 for 문이랑 합치기...
    for c in range(l):
        for r in range(l-n+1):
            tmp = ''
            for i in range(n):
                tmp += arr[r+i][c]
            if tmp == tmp[::-1]:
                cnt += 1
    return cnt

for t in range(1, 11):
    N = int(input())
    grid = []
    for _ in range(8):
        tmp = []
        tmp.extend(input())
        grid.append(tmp)
    result = ispalin(N, grid)
    print("#%d %d" % (t, result))

# 1230. [S/W 문제해결 기본] 8일차 - 암호문3
for t in range(1, 11):
    N = int(input())
    before = list(map(int, input().split()))
    M = int(input())
    S = list(input().split())
    for i in range(len(S)):
        if S[i] == 'I':
            # insert 하면 뒤로 계속 밀리니까 맨 끝 수부터 insert
            for j in range(int(S[i+2]), 0, -1):
                before.insert(int(S[i+1]), S[i+2+j])
        elif S[i] == 'D':
            for _ in range(int(S[i+2])):
                before.pop(int(S[i+1]))
        elif S[i] == 'A':
            # append는 맨 끝에서 차곡 차곡 붙으므로 순서대로 하면 됨
            for j in range(int(S[i+1])):
                before.append(int(S[i+2+j]))
    after = []
    for a in range(10):
        after.append(before[a])
    print("#%d %s" % (t, ' '.join(map(str, after))))

# 210224
# 1860. 진기의 최고급 붕어빵
T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    time = list(map(int, input().split()))
    # 시간 순서대로 판단하기 위해 정렬
    time.sort()
    result = 'Possible'
    # 이제까지 온 손님 수 cnt
    cnt = 0
    for i in time:
        # 해당 시점의 붕어빵 개수는 (i//M)*K 에서 손님 수를 뺀 값
        boonguh = (i//M)*K - cnt
        if boonguh == 0:
            result = 'Impossible'
            break
        # 붕어빵이 있으면 손님 수 +1
        else:
            cnt += 1
    print("#%d %s" % (t, result))

# 210225
# 4615. 재미있는 오셀로 게임
# drc 중복이었다... 실수 없게 꼼꼼히 확인..!
drc = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

def game(c, r, color):
    board[r][c] = color
    for i in range(8):
        nr = r+drc[i][0]
        nc = c+drc[i][1]
        check = []
        while True:
            # 이동한 인덱스가 범위 벗어나면 무효 - 임시 리스트 초기화 후 break
            if nr < 1 or nr > N or nc < 1 or nc > N:
                check = []
                break
            # 0이면 빈 자리이므로 무효 - 임시 리스트 초기화 후 break
            elif board[nr][nc] == 0:
                check = []
                break
            # 같은 색깔이면 break
            elif board[nr][nc] == color:
                break
            # 다른 색깔이면 임시 리스트에 인덱스 저장
            elif board[nr][nc] == 3 - color:
                check.append((nr, nc))
            # 해당 방향으로 한칸 더 이동
            nr += drc[i][0]
            nc += drc[i][1]
        # 반복 종료 후 임시 리스트에 있는 인덱스들을 color 칠함
        for x, y in check:
            board[x][y] = color

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    board = []
    for _ in range(N+2):
        board.append([0]*(N+2))
    mid = N//2
    board[mid][mid], board[mid+1][mid+1] = 2, 2
    board[mid][mid+1], board[mid+1][mid] = 1, 1
    for _ in range(M):
        c, r, color = map(int, input().split())
        game(c, r, color)
    # 색깔별로 개수 세기
    b, w = 0, 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if board[i][j] == 1:
                b += 1
            elif board[i][j] == 2:
                w += 1
    print("#%d %d %d" % (t, b, w))

# 210226
# 1209. [S/W 문제해결 기본] 2일차 - Sum
for _ in range(10):
    N = int(input())
    grid = []
    for _ in range(100):
        grid.append(list(map(int, input().split())))
    # print(grid)
    mx = 0
    # 행검사/열검사
    for r in range(100):
        tmp = 0
        for c in range(100):
            tmp += grid[r][c]
        # print(tmp)
        if tmp > mx:
            mx = tmp

        tmp = 0
        for c in range(100):
            tmp += grid[c][r]
        # print(tmp)
        if tmp > mx:
            mx = tmp

    drc = [[1, 1], [1, -1]]
    x, y = 0, 0
    dx, dy = drc[0][0], drc[0][1]
    # 대각선검사
    tmp = 0
    for i in range(100):
        tmp += grid[x+(dx*i)][y+(dy*i)]
    # print(tmp2)
    if tmp > mx:
        mx = tmp

    tmp = 0
    p, q = 0, 99
    dp, dq = drc[1][0], drc[1][1]
    for j in range(100):
        tmp += grid[p+(dp*j)][q+(dq*j)]
    # print(tmp3)
    if tmp > mx:
        mx = tmp

    print("#%d %d" % (N, mx))

# 4466. 최대 성적표 만들기
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    score = list(map(int, input().split()))
    # K번 선택정렬!
    for i in range(K):
        mx_idx = i
        for j in range(i+1, N):
            if score[j] > score[mx_idx]:
                mx_idx = j
        score[mx_idx], score[i] = score[i], score[mx_idx]

    result = sum(score[0:K])
    print(score)
    print("#%d %d" % (t, result))

# 210228
# 6019. 기차 사이의 파리
T = int(input())
for t in range(1, T+1):
    D, A, B, F = map(int, input().split())
    # 두 기차가 충돌하기까지 걸리는 시간 = x
    x = D/(A+B)
    # 파리의 속력에 x를 곱하면 답
    result = x*F
    print("#%d %.10f" % (t, result))

# 210302
# 1225. [S/W 문제해결 기본] 7일차 - 암호생성기
def make_pw(arr):
    l = [1, 2, 3, 4, 5]
    i = 0
    while True:
        x = arr.pop(0)
        if x-l[i] <= 0:
            arr.append(0)
            break
        else:
            arr.append(x-l[i])
        i += 1
        if i == 5:
            i = 0
    return arr

for _ in range(1, 11):
    N = int(input())
    code = list(map(int, input().split()))
    complete = ' '.join(map(str, make_pw(code)))
    print("#%d %s" % (N, complete))

# 1220. [S/W 문제해결 기본] 5일차 - Magnetic
for t in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    n_table = list(zip(*table))
    cnt = 0
    for r in range(N):
        last = 0
        for c in range(0, N):
            if n_table[r][c] == 2:
                if last == 1:
                    cnt += 1
                last = n_table[r][c]
            elif n_table[r][c] == 1:
                last = n_table[r][c]

    print("#%d %d" % (t, cnt))