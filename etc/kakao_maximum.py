import itertools
from copy import deepcopy
calc = {'+': lambda x,y: x+y,
        '-': lambda x,y: x-y,
        '*': lambda x,y: x*y}

def separate(nums, opslist):
    result = nums
    for o in opslist:
        for n in nums:
            if o in n:
                n = n.split(o)
    return nums
print(separate("100-200*300-500+20", ['*', '-', '+']))
nums = "100-200*300-500+20"
nums = nums.split('-')
nums = nums[2].split('+')
print(nums)

# def solution(expression):
#     answer = 0
#     ops = []
#     for i in expression:
#         if i in {'+', '-', '*'}:
#             ops.append(i)
#     pers = list(itertools.permutations(list(set(ops))))
#     for p in pers:
