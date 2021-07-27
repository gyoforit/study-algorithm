n = 50000
a = [False, False] + [True] * (n - 1)
primes = []

for i in range(2, n + 1):
    if a[i]:
        primes.append(i)
        for j in range(2 * i, n + 1, i):
            a[j] = False

primes = set(primes)


def solution(nums):
    answer = 0
    L = len(nums)
    for i in range(0, L - 2):
        for j in range(i + 1, L - 1):
            for k in range(j + 1, L):
                if nums[i] + nums[j] + nums[k] in primes:
                    answer += 1
    return answer