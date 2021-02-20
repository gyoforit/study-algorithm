# 백준 단계 10. 재귀
# 210212
# 10872. 팩토리얼
n = int(input())
def fac(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n*fac(n-1)

print(fac(n))

# 10870. 피보나치
n = int(input())
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(n))