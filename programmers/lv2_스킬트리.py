def solution(skill, skill_trees):
    ans = 0
    for skill_tree in skill_trees:
        stack = []
        for sk in skill_tree:
            if sk in skill:
                stack.append(sk)
        if stack:
            tmp = ''.join(stack)
            if tmp[0] == skill[0] and tmp in skill:
                ans += 1
        else:
            ans += 1

    return ans