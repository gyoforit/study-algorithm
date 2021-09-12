from itertools import permutations
def is_prime(x):
    if x < 2: return False
    elif x == 2: return True
    else:
        tmp = int(x**0.5)
        for i in range(2, tmp+1):
            if not x%i:
                return False
        return True

def solution(numbers):
    num_list = list(numbers)
    L = len(numbers)
    primes = set()
    for i in range(1, L+1):
        perms = set(permutations(num_list, i))
        for perm in perms:
            tmp = int(''.join(list(perm)))
            print(tmp)
            if is_prime(tmp):
                primes.add(tmp)
    return len(list(primes))