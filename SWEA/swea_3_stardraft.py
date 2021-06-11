# 미완성
# 1> 2, 2>3, 3> 1
def fight(a, b, arr):
    if (a[1] == 3 and b[1] == 1) or (a[1] == 1 and b[1] == 3):
        return arr.index(a) if a[1] > b[1] else arr.index(b)
    elif a[1] == b[1]:
        return arr.index(a) if a[0] < b[0] else arr.index(b)
    else:
        return arr.index(a) if a[1] < b[1] else arr.index(b)

def fight2(a, b):
    # print(a, b)
    if (a[1] == 3 and b[1] == 1) or (a[1] == 1 and b[1] == 3):
        return a if a[1] > b[1] else b
    elif a[1] == b[1]:
        return a if a[0] < b[0] else b
    else:
        return a if a[1] < b[1] else b

def league(arr):
    first_arr = []
    second_arr = []
    for start in list(range(len(arr)))[::4]:
        tmp = arr[start:start+4]
        score = [0]*4
        # print(tmp)
        for i in range(0, len(tmp)-1):
            for j in range(i+1, len(tmp)):
                score[fight(tmp[i], tmp[j], tmp)] += 1
        # print(score)
        first = score.index(max(score))
        # print(tmp[first])
        first_arr.append(tmp[first])
        tmp.pop(first)
        score.pop(first)
        # print(score)
        second = score.index(max(score))
        # print(tmp[second])
        second_arr.append(tmp[second])

    # print(first_arr)
    # print(second_arr)
    second_arr = second_arr[::-1]
    result = []
    for x in range(len(first_arr)):
        result.append(first_arr[x])
        result.append(second_arr[x])
    # print(result)
    return result

def get_winner(arr):
    # print(arr)
    if len(arr) == 1:
        # print('마지막')
        # print(arr[fight(arr[0], arr[1], arr)])
        return arr[0]
    else:
        mid = len(arr)//2
        a = get_winner(arr[:mid])
        b = get_winner(arr[mid:])
        # print(fight2(a, b))
        return fight2(a, b)
        # if a and b:
        #     tmp_arr = [a, b]
        #     print(tmp_arr)
        #     print('승자')
        #     print(get_winner(tmp_arr))
            # print(tmp_arr[fight(a, b, tmp_arr)])

T = int(input())
for t in range(1, T+1):
    teams = list(map(int, input().split()))
    new_teams = []
    for tm in range(len(teams)):
        new_teams.append((tm, teams[tm]))
    # print(new_teams)
    after_league = league(new_teams)
    # print(after_league)
    print("#%d %d" % (t, get_winner(after_league)[0]))
