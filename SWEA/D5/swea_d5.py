# 210418
# 1242. [S/W 문제해결 응용] 1일차 - 암호코드 스캔
password = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
        '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

# 암호코드 정상여부 판별 함수
def test(arr):
    result = 0
    for i in range(0, len(arr), 2):
            result += arr[i]*3
            result += arr[i+1]
    if result % 10:
        return 0
    else:
        return sum(arr)

# 이진수를 십진수로 변환하는 함수
def decode(arr, size):
    L = size*7*8
    temp = arr[-L:]
    complete = []
    for i in range(0, len(temp), size*7):
        num = password.get(temp[i:i+(size*7)][::size], 'X')
        if num == 'X':
            return 0
        complete.append(num)
    return tuple(complete)

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    check = set()
    answer = 0
    for _ in range(N):
        check.add(input()[:M].rstrip('0'))

    codelist = set()
    for code in check:
        if code:
            x = bin(int(code, 16))[2:].rstrip('0')
            while x:
                size = 1
                while True:
                    x = x.zfill(size*56)
                    result = decode(x, size)
                    if result != 0:
                        codelist.add(result)
                        L = size*7*8
                        x = x[:len(x)-L].rstrip('0')
                        break
                    size += 1

    print("#%d %d" % (t, sum(test(c) for c in codelist)))