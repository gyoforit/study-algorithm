# 백준 단계 1. 입출력과 사칙연산
# 210212
# 10718
for i in range(2):
    print("강한친구 대한육군")

# 10171
print("\    /\\\n )  ( \')\n(  /  )\n \\(__)|")

# 10172
print("|\\_/|\n|q p|   /}\n( 0 )\"\"\"\\\n|\"^\"`    |\n||_/=\\\\__|")

# 10998
A, B = map(int, input().split())
print(A*B)

# 1008
A, B = map(int, input().split())
print(A/B)

# 10869
A, B = map(int, input().split())
print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)
# 한 줄에 출력하는법
print(a+b,a-b,a*b,a//b,a%b,sep='\n')

# 10430
A, B, C = map(int, input().split())
print((A+B)%C, ((A%C)+(B%C))%C, (A*B)%C, ((A%C)*(B%C))%C, sep="\n")

# 2588
A = int(input())
B = input()
for i in range(2, -1, -1):
    print(A*int(B[i]))
print(A*int(B))