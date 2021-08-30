dic = {0: '', 1: 'A', 2: 'E', 3: 'I', 4: 'O', 5: 'U'}

def solution(word):
    ans = set()
    def combi(lv, w):
        if lv == 5:
            ans.add(''.join(w))
            return

        for i in range(6):
            w.append(dic[i])
            combi(lv + 1, w)
            w.pop()

    combi(0, [])
    ans = sorted(list(ans))
    return ans.index(word)
