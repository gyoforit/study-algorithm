# 백준 step2
# 1330. 두 수 비교하기
A, B = map(int, input().split())
if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("==")

# # 9498. 시험 성적
N = int(input())
if N >= 90:
    print("A")
elif N >= 80:
    print("B")
elif N >= 70:
    print("C")
elif N >= 60:
    print("D")
else:
    print("F")

# 2753. 윤년
N = int(input())
if (N % 4 == 0 and N % 100 != 0) or N % 400 == 0:
    print(1)
else:
    print(0)

# 14681. 사분면 고르기
x = int(input())
y = int(input())
if x*y > 0: # 1 or 3
    if x > 0:
        print(1)
    else:
        print(3)
else:
    if x > 0:
        print(4)
    else:
        print(2)

# 2884. 알람 시계
H, M = map(int, input().split())
if M >= 45:
    print("%d %d" % (H, M-45))
else:
    if H > 0:
        print("%d %d" % (H-1, 60-abs(M-45)))
    else:
        print("%d %d" % (23, 60 - abs(M - 45)))