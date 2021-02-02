# 210202
# 1945. 간단한 소인수분해
# T = int(input())
# for i in range(1, T+1):
#     a = 0
#     b = 0
#     c = 0
#     d = 0
#     e = 0
#     N = int(input())
#     while N > 1:
#         if N % 11 == 0:
#             e += 1
#             N = N//11
#         elif N % 7 == 0:
#             d += 1
#             N = N//7
#         elif N % 5 == 0:
#             c += 1
#             N = N//5
#         elif N % 3 == 0:
#             b += 1
#             N = N//3
#         elif N % 2 == 0:
#             a += 1
#             N = N//2
#     print(f"#{i} {a} {b} {c} {d} {e}")

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

import base64

N = 'Man'
binarychars = ''
binarylist = []
for char in N:
    bin_char = ''
    asc = ord(char)
    bin_char += bin(asc)[2:]
    while len(bin_char) < 8:
        bin_char = '0' + bin_char
        binarychars += bin_char
# 01001101011... 출력
# # print(type(binarychars))
binarylist.extend(binarychars)
for i in range(len(binarylist)//6 -1):
    chars6 = []
    chars6int = ''
    chars6 += binarylist[6*i:6*(i+1)]
    # print(''.join(chars6))
    chars6int += '0b' + ''.join(chars6)
    x = str(int(chars6int, 2))

# ascii 이용하여 index 값 구하기
# index를 이진수로 바꿔서 나열하기
# 8개씩 slicing해서 10진수로 변환
# ascii 이용하여 다시 변환

N = 'TWFu'
for char in N:
    print(ord(char))
    


# 1986. 지그재그 숫자
# 1284. 수도 요금 경쟁
# 1288. 새로운 불면증 치료법
# 1989. 초심자의 회문 검사
# 1959. 두 개의 숫자열
# 1948. 날짜 계산기
# 2007. 패턴 마디의 길이
# 1979. 어디에 단어가 들어갈 수 있을까