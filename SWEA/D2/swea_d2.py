# 210202
# 1945. 간단한 소인수분해
T = int(input())
for i in range(1, T+1):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    N = int(input())
    while N > 1:
        if N % 11 == 0:
            e += 1
            N = N//11
        elif N % 7 == 0:
            d += 1
            N = N//7
        elif N % 5 == 0:
            c += 1
            N = N//5
        elif N % 3 == 0:
            b += 1
            N = N//3
        elif N % 2 == 0:
            a += 1
            N = N//2
    print(f"#{i} {a} {b} {c} {d} {e}")

# 1928. Base64 Decoder

# 아스키코드로 변환
# 변환한 숫자를 2진수로 변환
# 숫자부분만 떼어냄
# 만약 숫자 길이가 8이 아니라면 앞에 0붙이기
# 모든 숫자를 다 이어붙이기!
# 6개씩 슬라이싱 해서 다시 10진수 변환
# 이를 알파벳으로 변환....

# 이걸 거꾸로 해야됨...^^
# format, rjust 배워서 써먹기!

# import base64

# N = 'Man'
# binarychars = ''
# binarylist = []
# for char in N:
#     bin_char = ''
#     asc = ord(char)
#     bin_char += bin(asc)[2:]
#     while len(bin_char) < 8:
#         bin_char = '0' + bin_char
#         binarychars += bin_char
# # 01001101011... 출력
# # # print(type(binarychars))
# binarylist.extend(binarychars)
# for i in range(len(binarylist)//6 -1):
#     chars6 = []
#     chars6int = ''
#     chars6 += binarylist[6*i:6*(i+1)]
#     # print(''.join(chars6))
#     chars6int += '0b' + ''.join(chars6)
#     x = str(int(chars6int, 2))

# ascii 이용하여 index 값 구하기
# index를 이진수로 바꿔서 나열하기
# 8개씩 slicing해서 10진수로 변환
# ascii 이용하여 다시 변환

# N = 'TWFu'
# for char in N:
#     print(ord(char))

# 210204  
# 1986. 지그재그 숫자
T = int(input())
for i in range(1, T+1):
    N = int(input())
    result = 0
    for n in range(1, N+1):
        if n % 2:
            result += n
        else:
            result -= n
    print(f"#{i} {result}")

# 1284. 수도 요금 경쟁
T = int(input())
for i in range(1, T+1):
    numbers = list(map(int, input().split()))
    A = 0
    B = 0
    result = 0
    A = numbers[0]*numbers[4] # P*W
    if numbers[4] <= numbers[2]: # W<=R
        B = numbers[1] # Q
    else:
        B = numbers[1] + numbers[3]*(numbers[4]-numbers[2])
    result = min(A, B)
    print(f"#{i} {result}")
# 문제 제대로 읽기!!! 최소요금!!!

# 1288. 새로운 불면증 치료법
T = int(input())
for i in range(1, T+1):
    N = int(input())
    numbers = set()
    count = 0
    while len(numbers) < 10:
        count += 1
        M = N*count
        num = []
        num.extend(str(M))
        for idx in range(len(num)):
            numbers.update(num)
    print(N*count)
# 이것도 문제 좀 제대로....ㅠㅠ

# 채은님 풀이(list에 넣어서 set 변환하면 어차피 중복된거 빠짐)
T = int(input())
for t in range(1, T+1):
    N = int(input())
    cn = 1
    lst = []
    while set(lst) != set(range(10)):
        for n in str(N * cn):
            lst.append(int(n))
        cn += 1
    print(f'#{t} {(cn-1) * N} ')

# 주엽님 아이디어 활용 (숫자 없애기)
T = int(input())
for i in range(1,T+1):
    count = 0
    N = input()
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    while numbers != []:
        count += 1
        M = str(int(N)*count)
        for num in M:
            if int(num) in numbers:
                numbers.remove(int(num))
    print(f"#{i} {int(N)*count}")

# 1989. 초심자의 회문 검사
T = int(input())
for i in range(1, T+1):
    chars = input()
    while len(chars) > 2:
        if chars[0] != chars[-1]:
            print(f"#{i} 0")
            break
        else:
            chars = chars[1:-1]
    else:
        print(f"#{i} 1")

# 210208
# 1966. 숫자를 정렬하자
T = int(input())
for t in range(1, T+1):
    N = int(input())
    nb = list(map(int, input().split()))
    result = ''
    for i in range(0, N-1):
        for j in range(i+1, N):
            if nb[i] > nb[j]:
                nb[j], nb[i] = nb[i], nb[j]
    for a in range(len(nb)):
        nb[a] = str(nb[a])
    result = ' '.join(nb)
    print('#%d %s' % (t, result))

# 1970. 쉬운 거스름돈
'''
단위별로 돌아가며 N과 비교.
N이 더 크면 N으로 나눈 몫을 count (해당 돈의 개수니까)
그리고 나머지를 다시 N에다 집어넣음
'''
T = int(input())
for t in range(1, T+1):
    N = int(input()) #32850
    mn = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = [0, 0, 0, 0, 0, 0, 0, 0]
    ans = ''
    for i in range(len(mn)):
        if N >= mn[i]:
            result[i] = N // mn[i]
            N = N % mn[i]
        else:
            result[i] = 0
    for n in range(len(result)):
        result[n] = str(result[n])
    ans = ' '.join(result)
    print('#%d\n%s' % (t, ans))

# 210209
# 1948. 날짜계산기
'''
월/일을 단순히 일로만 계산하는 함수 작성
'''
def howmanydate(m, d):
    result = 0
    if m == 1:
        return d
    else:
        a = 1
        while a < m:
            if a in [1, 3, 5, 7, 8, 10, 12]:
                result += 31
                a += 1
            elif a in [4, 6, 9, 11]:
                result += 30
                a += 1
            elif a == 2:
                result += 28
                a += 1
        return result + d

T = int(input())
for t in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())
    print(f'#{t} {howmanydate(m2, d2) - howmanydate(m1, d1) + 1}')

# 210210
# 1959. 두 개의 숫자열
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split()) # M이 크다고 가정!
    Nlist = list(map(int, input().split()))
    Mlist = list(map(int, input().split()))
    if N > M:
        N, M = M, N
        Nlist, Mlist = Mlist, Nlist

    mx = float('-inf')
    for i in range(0, M-N+1): # C의 초깃값
        C = []
        for j in range(i, i+N):
            C += [Mlist[j]]

        tmp = 0
        for a in range(N):
            tmp += Nlist[a] * C[a]
        if tmp > mx:
            mx = tmp
    print('#%d %d' % (t, mx))

# 다른 풀이
def check(long, short):
    max_value = -987654321
    for i in range(len(long)-len(short)+1): # 큰 숫자열을 작은 숫자열 길이만큼 자를건데 그 시작 부분의 pointer 역할
        result = 0 # for 문 안에서 초기화를 해야 함. 매 pointer가 바뀔 때마다 새롭게 곱할 값의 합을 알아봐야 하니깐!
        for j in range(len(short)): # 작은 숫자열의 인덱스 차례로 돌면서
            result += long[i+j]*short[j] # 곱한다! 큰 숫자열에는 위에서 구한 시작점을 더해줘서 매 싸이클 마다 달라지게..

        if max_value < result:
            max_value = result
    return max_value

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N > M:
        ans = check(A, B)
    else:
        ans = check(B, A)

    print("#{} {}".format(tc, ans))

# 210215
# 1943. 달팽이 숫자
# 델타 사용한 풀이
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    result = []
    for a in range(N):
        result.append([0] * N)
    # 현위치
    r = 0
    c = -1
    # 배열에 넣을 숫자
    n = 0
    # 반복 횟수
    k = N
    # 델타(방향키)
    drc = [[0, 1, 0, -1], [1, 0, -1, 0]]
    # 델타의 인덱스
    a = 0
    # k를 -1 할지 말지 결정하는 cnt
    cnt = 0
    # 종료조건 만족할 때까지 무한 반복
    while True:
        # 행 고정, 열 이동
        for i in range(1, k + 1):
            n += 1
            r += drc[0][a]
            c += drc[1][a]
            result[r][c] = n
        # cnt +1 한 다음 cnt가 홀수면 k를 -1 감소
        cnt += 1
        if cnt % 2:
            k -= 1
        # 반복문 종료 조건
        if k <= 0:
            break
        # 방향키 변경(델타 인덱스 +1)
        a += 1
        # 델타 인덱스가 범위 밖을 벗어나는 오류 방지(끝까지 가면 다시 0으로 초기화)
        if a > 3:
            a = 0
    print("#%d" % t)
    for i in range(N):
        print(' '.join(map(str, result[i])))

# 델타 사용하지 않은 풀이
T = int(input())
for t in range(1, T+1):
    N = int(input())
    result = []
    for a in range(N):
        result.append([0]*N)
    # 현 위치
    r = 0
    c = -1
    # 배열에 들어갈 숫자
    n = 0
    # r, c의 방향키 역할(순방향/역방향)
    d = 1
    # 반복횟수
    k = N
    # 반복문 종료조건 만족할 때까지 무한 반복
    while True:
        # 행 고정, 열 이동
        for i in range(1, k+1):
            n += 1
            c += d
            result[r][c] = n
        # 반복횟수 -1
        k -= 1
        # 종료 조건
        if k <= 0:
            break
        # 열 고정, 행 이동
        for i in range(1, k+1):
            n += 1
            r += d
            result[r][c] = n
        # 방향 바꿈
        d *= -1

    # print(result)
    print("#%d" % t)
    for i in range(N):
        print(' '.join(map(str, result[i])))

# 210216
# 1979. 어디에 단어가 들어갈 수 있을까
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    # 가로세로판 만들기
    grid = []
    for g in range(N):
        grid.append(list(map(int, input().split())))
    # 단어가 들어갈 수 있는 경우의 수 세는 용
    cnt = 0
    # 행 고정, 열 탐색
    for r in range(N):
        # 해당 열에서의 1이 있는 길이 측정하기 위한 l 초기화
        l = 0
        for c in range(N):
            # 1이면 l에 +1
            if grid[r][c] == 1:
                l += 1
            # 0이면 앞에까지 더해놨던 l 파악 -> 만약 K라면 cnt +1 한 후에 l을 다시 0으로 초기화
            else:
                if l == K:
                    cnt += 1
                l = 0
        # 마지막 열이 l인 경우를 위해 다시 한번 K랑 같은지 파악
        if l == K:
            cnt += 1
    # 열 고정, 행 탐색 (똑같음)
    for c in range(N):
        l = 0
        for r in range(N):
            if grid[r][c] == 1:
                l += 1
            else:
                if l == K:
                    cnt += 1
                l = 0
        if l == K:
            cnt += 1
    print("#%d %d" % (t, cnt))

# 2001. 파리퇴치
T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    # 이중 배열 만들기
    grid = []
    for n in range(N):
        grid.append(list(map(int, input().split())))
    # 최댓값 저장할 mx
    mx = 0
    # 기준 위치 r, c
    r = 0
    c = 0
    while True:
        # 해당 구간에서의 요소 합 구할 tmp
        tmp = 0
        # 좌상단 모서리를 r, c라고 했을 때 M*M 파리채 만들어서 해당하는 요소들 모두 tmp에 더함
        for i in range(r, r + M):
            for j in range(c, c + M):
                tmp += grid[i][j]
        # tmp가 mx보다 크면 mx에 tmp 할당 후 열을 한칸 이동( c +1 )
        if tmp > mx:
            mx = tmp
        c += 1
        # 열을 계속 더하다가 N-M 보다 커지면 0열로 돌아가고 r을 한칸 +1
        if c == N - M + 1:
            r += 1
            c = 0
        # 좌상단 모서리의 r이 제일 마지막 위치(N-M)의 좌표보다 커지면 반복 종료
        if r > N - M:
            break
    print("#%d %d" % (t, mx))

# 1940. 가랏! RC카!
T = int(input())
for t in range(1, T+1):
    N = int(input())
    now = 0
    vc = 0
    for n in range(N):
        try:
            a, b = map(int, input().split())
            if a == 1:
                vc += b
                now += vc
            elif a == 2:
                if b > vc:
                    vc = 0
                else:
                    vc -= b
                now += vc
        except:
            now += vc
    print("#%d %d" % (t, now))

# 1976. 시각 덧셈
T = int(input())
for t in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())
    h, m = 0, 0
    if m1 + m2 >= 60:
        m = m1+m2-60
        if h1+h2 > 12:
            h = h1+h2-11
        else:
            h = h1+h2+1
    else:
        m = m1+m2
        if h1+h2 > 12:
            h = h1+h2-12
        else:
            h = h1+h2
    print("#%d %d %d" % (t, h, m))

# 210217
#1974. 스도쿠검증
# 겹치는게 하나라도 있으면 무조건 0이므로 return False가 더 먼저 나와야 함
# 행 검사하는 함수
def test_row(arr):
    N = len(arr)
    for r in range(N):
        test = []
        for c in range(N):
            test.append(arr[r][c])
        if len(set(test)) != 9:
            return False
    else:
        return True
# 열 검사하는 함수
def test_col(arr):
    N = len(arr)
    for c in range(N):
        test = []
        for r in range(N):
            test.append(arr[r][c])
        if len(set(test)) != 9:
            return False
    return True
# 3*3 네모 검사하는 함수
def test_sqr(arr):
    r = 0
    c = 0
    while True:
        test = []
        for i in range(r, r+3):
            for j in range(c, c+3):
                test.append(arr[i][j])
        if len(set(test)) != 9:
            return False
        else:
            c += 3
        if c == 9:
            c = 0
            r += 3
        if r == 9:
            break
    return True

T = int(input())
for t in range(1, T+1):
    puzzle = []
    L = 9
    for i in range(9):
        puzzle.append(list(map(int, input().split())))
    if test_row(puzzle) and test_col(puzzle) and test_sqr(puzzle):
        print("#%d 1" % t)
    else:
        print("#%d 0" % t)

# 210218
# 4861. 회문
# 회문인지 판단하는 함수 정의
def ispalin(x):
    if len(x) <= 1:
        return True
    while len(x) > 1:
        if x[0] == x[-1]:
            return ispalin(x[1:-1])
        else:
            return False

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    # 그리드 만들기
    grid = []
    for n in range(N):
        tmp = []
        tmp.extend(input())
        grid.append(tmp)
    # 찾자마자 반복 끝내기 위해 while 문 안에 flag 장치를 둠
    while True:
        flag = 0
        # 행 고정
        for r in range(N):
            for c in range(N-M+1):
                tmp = ''
                for i in range(M):
                    tmp += grid[r][c+i]
                if ispalin(tmp):
                    flag = 1
                    print("#%d %s" % (t, tmp))
                    break
        if flag == 1:
            break
        # 열 고정
        for c in range(N):
            for r in range(N-M+1):
                tmp = ''
                for i in range(M):
                    tmp += grid[r+i][c]
                if ispalin(tmp):
                    print("#%d %s" % (t, tmp))
                    break
        break

# 4864. 문자열 비교
def compare(A, B):
    a = len(A)
    b = len(B)
    for i in range(b-a+1):
        if B[i] == A[0]:
            if B[i:i+a] == A:
                return 1
    else:
        return 0

T = int(input())
for t in range(1, T+1):
    N = input()
    M = input()
    result = compare(N, M)

    print("#%d %d" % (t, result))

# 4865. 글자수
T = int(input())
for t in range(1, T+1):
    str1 = []
    str1.extend(input())
    str2 = input()
    str_dict = dict.fromkeys(str1, 0)

    for s in str2:
        if s in str_dict.keys():
            str_dict[s] += 1
    result = max(str_dict.values())
    print("#%d %d" % (t, result))

# 1926. 간단한 369 게임
# 3, 6, 9 개수 세는 함수
def cnt(n):
    result = n.count('3') + n.count('6') + n.count('9')
    return result

N = int(input())
for i in range(1, N+1):
    tmp = []
    # 숫자 하나씩 확인하기 위해 string 으로 받아서 extend
    tmp.extend(str(i))
    if cnt(tmp) == 0:
        print(i, end =' ')
    else:
        print('-'*cnt(tmp), end = ' ')

# 1983. 조교의 성적 매기기
scr = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
# 총점 세는 함수 정의
def score(m, f, h):
    total = m*0.35 + f*0.45 + h*0.2
    return total

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    score_list = []
    student = 0
    for n in range(N):
        m, f, h = map(int, input().split())
        s = score(m, f, h)
        score_list.append(s)
    # 등수 확인하고 싶은 번호의 점수를 student에 저장
    student = score_list[M-1]
    rank = 0
    sorted_list = sorted(score_list) # 오름차순
    for a in range(N):
        # 해당 점수의 등수를 뽑음
        if sorted_list[a] == student:
            rank = N-a # 오름차순에서 8등은 상위 2등이기 때문
            break

    if rank % (N//10) != 0:
        rank = rank//(N//10) + 1
    else:
        rank = rank//(N//10)
    print("#%d %s" % (t, scr[int(rank-1)]))

# 1946. 압축풀기
T = int(input())
for t in range(1, T+1):
    N = int(input())
    text = ''
    for n in range(N):
        c, k = input().split()
        text += c*int(k)
    # 한번에 쭉 길게 늘어뜨린다음
    txt = len(text)
    i = 0
    print("#%d" % t)
    # 10개 단위로 잘라서 print (slicing 에서는 index 벗어나도 되는 점을 이용)
    while True:
        print(text[i:i+10])
        i += 10
        if i > txt:
            break

# 1984. 중간 평균값 구하기
def get_max(arr):
    mx = arr[0]
    for i in arr:
        if i > mx:
            mx = i
    return mx

def get_min(arr):
    mn = arr[0]
    for i in arr:
        if i < mn:
            mn = i
    return mn

T = int(input())
for t in range(1, T+1):
    num = list(map(int, input().split()))
    num.remove(get_max(num))
    num.remove(get_min(num))
    total = 0
    n = len(num)
    for i in num:
        total += i
    result = total/n
    print("#%d %d" % (t, int(round(result, 0))))

# 1204. 최빈수 구하기
T = int(input())
for t in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    cnt = [0] * 101
    for n in num:
        cnt[n] += 1
    mx_idx = 0

    for i in range(101):
        if cnt[i] >= cnt[mx_idx]:
            mx_idx = i
    print("#%d %d" % (t, mx_idx))

# 210219
# 1961. 숫자 배열 회전
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = []
    for a in range(N):
        arr.append(list(input().split()))
    print("#%d" % t)
    # i, j는 고정해놓고 각 회전에 따라 i, j를 사용하여 다르게 표현하기
    for i in range(N):
        tmp = ''
        for j in range(N):
            tmp += arr[N-1-j][i]
        tmp += ' '
        for j in range(N):
            tmp += arr[N-1-i][N-1-j]
        tmp += ' '
        for j in range(N):
            tmp += arr[j][N-1-i]
        print(tmp)

# 210222
# 2005. 파스칼의 삼각형
T = int(input())
for t in range(1, T+1):
    pascal = []
    N = int(input())
    for n in range(1, N+1):
        if n == 1:
            pascal.append([1])
        elif n == 2:
            pascal.append([1, 1])
        elif n >= 3:
            tmp = []
            # 바로 이전 리스트의 요소들을 둘씩 더한 값을 tmp에 저장
            for i in range(n-2):
                tmp += [pascal[n-2][i]+pascal[n-2][i+1]]
            # tmp의 양 옆을 1로 감싸서 append
            tmp = [1] + tmp + [1]
            pascal.append(tmp)
    print("#%d" % t)
    for a in range(N):
        print(' '.join(map(str, pascal[a])))

# 11572. 괄호검사
# 열린 괄호와 닫힌 괄호를 인덱스로 구별하기 위한 리스트 생성
opn = ['(', '{', '[']
cls = [')', '}', ']']
T = int(input())
for t in range(1, T + 1):
    bracket = []
    # 규칙에 어긋나면 0으로 바뀜
    result = 1
    S = input()
    for s in S:
        # 열린 괄호일 때: 소/중/대 종류에 맞는 인덱스를 append
        if s in opn:
            for i in range(len(opn)):
                if opn[i] == s:
                    bracket.append(i)
                    break
        # 닫힌 괄호일 때: 가장 최근에 append 된 요소를 비교하여 같으면 pop
        elif s in cls:
            # bracket이 비어있다 = 짝이 안 맞는다 = 규칙에 어긋남
            if len(bracket) == 0:
                result = 0
                break
            else:
                tmp = 0
                poped = bracket.pop(-1)
                for j in range(len(cls)):
                    if cls[j] == s:
                        tmp = j
                # 가장 최근에 append 된 요소와 닫힌 괄호의 종류가 다르면 규칙에 어긋남
                if tmp != poped:
                    result = 0
                    break
    # 문자열을 다 돌았는데 bracket에 요소가 있음 = 짝이 안 맞는다 = 규칙에 어긋남
    if len(bracket) > 0:
        result = 0

    print("#%d %d" % (t, result))

# 210223
# 4871. [파이썬 S/W 문제해결 기본] 4일차 - 그래프 경로
# 인접 행렬 이용
T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    AM = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        AM[s][e] = 1
    S, G = map(int, input().split())
    stack = [S]
    visited = [0]*(V+1)
    result = 0
    while stack:
        now = stack.pop()
        if not visited[now]:
            visited[now] = 1
            if now == G:
                result = 1
                break
            for i in range(1, V+1):
                if AM[now][i] == 1 and visited[i] == 0:
                    stack.append(i)
    print("#%d %d" % (t, result))

# 인접 리스트 이용
T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    AL = [[] for _ in range(V+1)]
    for _ in range(E): # E번 반복
        s, e = map(int, input().split())
        AL[s].append(e)
    S, G = map(int, input().split())
    stack = [S]
    visited = [0]*(V+1)
    result = 0
    while stack:
        now = stack.pop()
        if not visited[now]:
            visited[now] = 1
            if now == G:
                result = 1
                break
            for i in AL[now]:
                if not visited[i]:
                    stack.append(i)
    print("#%d %d" % (t, result))

# 4873. [파이썬 S/W 문제해결 기본] 4일차 - 반복문자 지우기
T = int(input())
for t in range(1, T+1):
    S = input()
    stack = []
    for s in S:
        if not stack:
            stack.append(s)
        else:
            last = stack[-1]
            if last != s:
                stack.append(s)
            else:
                stack.pop()

    print("#%d %d" % (t, len(stack)))

# 좀 더 간결하게 수정
T = int(input())
for t in range(1, T+1):
    S = input()
    stack = []
    for s in S:
        if not stack or stack[-1] != s:
            stack.append(s)
        else:
            stack.pop()
    l = len(stack)
    print("#%d %d" % (t, l))

# 4869. [파이썬 S/W 문제해결 기본] 4일차 - 종이붙이기
# DP 활용! 바로 전, 전전 것에서 규칙을 찾는다.
def paper(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    if n > 2:
        return paper(n-1)+(paper(n-2)*2)
T = int(input())
for t in range(1, T+1):
    N = int(input())
    result = paper(N//10)
    print("#%d %d" % (t, result))

# 210224
# 1859. 백만장자 프로젝트
# 리스트의 max 기준으로 한 번 잘라서 이익 구하고, 그 다음 인덱스부터 max를 또 구하고 ...(반복)
# 맨 뒤에서부터 접근하면 간단함 - 더 큰 값 나올 때까지 누적해서 이익 더하기
T = int(input())
for t in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    mx_now = price[-1]
    money = 0
    for i in range(N-2, -1, -1):
        if mx_now > price[i]:
            money += mx_now - price[i]
        else:
            mx_now = price[i]
    print("#%d %d" % (t, money))

# 11556. 부분집합의 합 - 재귀 사용
A = list(range(1, 13))
n = 12

def DFS_subset(lv, C, S):
    # 성능 향상을 위한 가지치기
    if C > N or S > K: return
    # 종료조건
    if lv == n:
        if C == N and S == K:
            global cnt
            cnt += 1
        return

    DFS_subset(lv+1, C+1, S + A[lv])
    DFS_subset(lv+1, C, S)

T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    cnt = 0
    DFS_subset(0, 0, 0)
    print('#%d %d' % (t, cnt))

# 210302
# 4875. [파이썬 S/W 문제해결 기본] 5일차 - 미로
# 재귀 안 쓴 풀이
drc = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def DFS_maze(arr, sr, sc):
    visited = []
    stack = [(sr, sc)]
    # 경로 유무 정보를 담는 flag
    flag = 0
    while stack:
        # stack에서 pop한 요소를 현재 위치로 설정
        now_r, now_c = stack.pop()
        # 현재 위치를 방문하지 않았다면 방문 체크 후 도착점인지 확인
        if (now_r, now_c) not in visited:
            visited.append((now_r, now_c))
            # 도착점이면 flag를 1로 바꾼 후 break
            if arr[now_r][now_c] == 3:
                flag = 1
                break
        # 현재 위치에서 상하좌우 살펴봄
        for i in range(4):
            nr = now_r+drc[i][0]
            nc = now_c+drc[i][1]
            # 이동하고자 하는 위치가 1이 아닌 동시에 방문한 곳이 아니라면 stack에 append
            if arr[nr][nc] != 1 and (nr, nc) not in visited:
                stack.append((nr, nc))
    return flag

T = int(input())
for t in range(1, T+1):
    N = int(input())
    maze = [[1]+list(map(int, input()))+[1] for _ in range(N)]
    maze.insert(0, [1]*(N+2))
    maze.append([1]*(N+2))
    sr, sc = 0, 0
    # 시작점의 행/열 인덱스 찾기
    for r in range(1, N+1):
        for c in range(1, N+1):
            if maze[r][c] == 2:
                sr, sc = r, c
                break
    result = DFS_maze(maze, sr, sc)
    print("#%d %d" % (t, result))

# 4874. [파이썬 S/W 문제해결 기본] 5일차 - Forth
def forth(arr):
    stack = []
    for c in arr:
        if c not in "+-*/.":
            stack.append(c)
        elif c == '.':
            # . 나왔을 때 stack의 길이 확인. 1개보다 많으면 error
            if len(stack) == 1:
                return stack.pop()
            else:
                return "error"
        elif c in "+-*/":
            # 연산자가 나왔을 때 stack 속 요소가 2개보다 적으면 error
            if len(stack) < 2:
                return "error"
            else:
                B = int(stack.pop())
                A = int(stack.pop())
                if c == '+':
                    stack.append(A + B)
                elif c == '-':
                    stack.append(A - B)
                elif c == '*':
                    stack.append(A * B)
                else:
                    # (혹시몰라서) 나누는 숫자가 0이면 zero division으로 error
                    if B == 0:
                        return "error"
                    else:
                        stack.append(int(A/B))

T = int(input())
for t in range(1, T+1):
    calc = input().split()
    result = forth(calc)
    print("#%d %s" % (t, result))

# 4880. [파이썬 S/W 문제해결 기본] 5일차 - 토너먼트 카드게임
# 가위바위보 게임하는 함수
def game(a, b):
    if (cards[a], cards[b]) == (1, 3) or (cards[a], cards[b]) == (2, 1) or (cards[a], cards[b]) == (3, 2):
        return a
    elif cards[a] == cards[b]:
        return a
    else:
        return b

# 토너먼트 매칭시키는 함수
def tnmt(s, e):
    # 종료조건: 한명만 남으면 리턴
    if s == e:
        return s
    else:
        mid = (s+e)//2
        first = tnmt(s, mid)
        second = tnmt(mid+1, e)
        return game(first, second)


T = int(input())
for t in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))
    winner = tnmt(0, N-1) + 1
    print("#%d %d" % (t, winner))

# 4881. [파이썬 S/W 문제해결 기본] 5일차 - 배열 최소 합
# 열 인덱스를 순열로 뽑아내기
def minsum(r):
    global tmp, mn
    # 제한시간 초과 방지: 최솟값보다 크면 return
    if tmp > mn:
        return
    # 최솟값보다 작으면 새로 갱신
    if r == N:
        if tmp < mn:
            mn = tmp
        return
    # 인덱스 뽑아내는 동시에 해당 순열에 따른 배열 합 구함
    for c in range(N):
        if check[c] == 0:
            check[c] = 1
            tmp += num[r][c]
            minsum(r+1)
            check[c] = 0
            tmp -= num[r][c]

T = int(input())
for t in range(1, T+1):
    N = int(input())
    num = [list(map(int, input().split())) for _ in range(N)]
    check = [0]*N
    tmp, mn = 0, 10000000
    minsum(0)
    print("#%d %d" % (t, mn))

# 210303
# 11624. 큐
front = -1
rear = -1
N = 3
queue = [0] * N
def enQueue(queue, data):
    global rear
    if rear >= N-1:
        print("Queue overflow")
        return
    rear += 1
    queue[rear] = data

def deQueue(queue):
    global front
    front += 1
    if front == rear:
        print("Queue underflow")
        return
    return queue[front]

T = int(input())
num = map(int, input().split())
for n in num:
    enQueue(queue, n)
result = ' '.join(map(str, queue))
print("#%d %s" % (T, result))

# 11625. BFS
def BFS(s):
    visited = [0]*(V+1)
    queue = []
    visit = []  # 이동 경로 파악용 리스트
    visited[s] = True
    queue.append(s)
    while queue:
        target = queue.pop(0)
        visit.append(target)
        for x in AL[target]:
            if visited[x]: continue
            visited[x] = True
            queue.append(x)
    return visit

T = int(input())
V, E = map(int, input().split())
AL = [[] for _ in range(V+1)]
for _ in range(E):
    m, n = map(int, input().split())
    AL[m].append(n)
route = ' '.join(map(str, BFS(1)))
print("#%d %s" % (T, route))

# 210304
# 5102. [파이썬 S/W 문제해결 기본] 6일차 - 노드의 거리
def BFS(s, e):
    visited = [0]*(V+1)
    queue = []
    distance = [0]*(V+1)
    queue.append(s)
    visited[s] = True
    distance[s] = 0
    cnt = 1
    while queue:
        for _ in range(len(queue)):
            target = queue.pop(0)
            for x in AL[target]:
                if visited[x]: continue
                visited[x] = True
                distance[x] = cnt
                queue.append(x)
        cnt += 1
    return distance[e]

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    AL = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        AL[s].append(e)
        AL[e].append(s) # 무방향(양방향) 일 때 이것도 꼭 써줘야 함!
    S, E = map(int, input().split())

    print("#%d %s" % (t, BFS(S, E)))

# 210406
# 11748. 파이썬 SW문제해결 기본 - Tree 8일차 subtree
# child가 없으면 알아서 for문 안 도니까 이렇게 바꿔도 된다!
def subtree(n):
    global cnt
    cnt += 1
    for c in tree[n]:
        subtree(c)
    return

T = int(input())
for t in range(1, T+1):
    E, N = map(int, input().split())
    nums = list(map(int, input().split()))
    tree = [[] for _ in range(E+2)]
    for i in range(E):
        tree[nums[2*i]].append(nums[2*i+1])
    cnt = 0
    subtree(N)
    print("#%d %d" % (t, cnt))

# 11749. 파이썬 SW문제해결 기본 - Tree 8일차 - 이진탐색
def insert(n):
    global i
    if n <= N:
        insert(2*n)
        tree[n] = i
        i += 1
        insert(2*n+1)
    return

for t in range(1, int(input())+1):
    N = int(input())
    tree = [0]*(N+1)
    i = 1
    insert(i)
    print("#%d %d %d" % (t, tree[1], tree[N//2]))

# 11758. [파이썬 S/W 문제해결 기본] 8일차 - 이진 힙
def insert(x, i):
    p_idx = i//2
    p = tree[p_idx]
    # 부모에 x 등록
    if p[0]:
        idx = 2 if p[1] else 1
        p[idx] = i
        if p[0] > x:
            while p[0] > x:
                tmp = p[0]
                p[0] = x
                tree[i][0] = tmp
                p_idx = p_idx//2
            return
    tree[i][0] = x
    return

T = int(input())
for t in range(1, T+1):
    N = int(input())
    tree = [[0, 0, 0] for _ in range(N+1)]
    nums = list(map(int, input().split()))
    for n in range(N):
        insert(nums[n], n+1)

    result = 0
    parent = N//2
    while parent != 0:
        result += tree[parent][0]
        parent //= 2
    print("#%d %d" % (t, result))

# 11759. [파이썬 S/W 문제해결 기본] 8일차 - 노드의 합
def save(n):
    if 2*n <= N and tree[2*n] == 0:
        save(2*n)
    if 2*n+1 <= N and tree[2*n+1] == 0:
        save(2*n+1)
    l = 0 if 2*n > N else tree[2*n]
    r = 0 if 2*n+1 > N else tree[2*n+1]
    tree[n] = l+r
    return

T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0]*(N+1)
    for _ in range(M):
        a, b = map(int, input().split())
        tree[a] = b
    save(1)
    print("#%d %d" % (t, tree[L]))

# 210407
# 1966. 숫자를 정렬하자 (머지소트)
def merge_sort(a):
    if len(a) == 1:
        return a
    mid = len(a) // 2
    # print(mid, a)
    arr = merge_sort(a[:mid]) # arr, brr은 정렬된 두 개의 배열
    brr = merge_sort(a[mid:])
    # print(arr, brr)
    # arr, brr을 합쳐서 하나의 정렬된 배열을 만듦
    temp = []
    ai, bi = 0, 0
    while ai < len(arr) and bi < len(brr):
        if arr[ai] < brr[bi]:
            temp.append(arr[ai])
            ai += 1
        else:
            temp.append(brr[bi])
            bi += 1
    temp += arr[ai:]
    temp += brr[bi:]
    # print(temp)
    return temp

# a = [5, 1, 9, 6, 8, 4, 2, 3]
# merge_sort(a)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    result = merge_sort(nums)
    print("#%d %s" % (t, ' '.join(map(str, result))))

# 11792. [파이썬 S/W 문제해결 구현] 1일차 - 이진수
T = int(input())
for t in range(1, T+1):
    N, num = input().split()
    result = ''
    for n in range(int(N)):
        result += str(bin(int(num[n], 16))[2:]).zfill(4)
    print("#%d %s" % (t, result))

# 11794. [파이썬 S/W 문제해결 구현] 1일차 - 이진수2
T = int(input())
for t in range(1, T+1):
    N = float(input())
    result = ''
    for i in range(1, 13):
        dvd = 1/(1<<i)
        if N == 0:
            break
        if N >= dvd:
            result += '1'
            N -= dvd
        else:
            result += '0'
    else:
        result = 'overflow'
    print("#%d %s" % (t, result))