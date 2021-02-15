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
