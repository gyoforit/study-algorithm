T = int(input())
for t in range(1, T+1):
    n = int(input())
    nums = []
    max_num_idx = 0
    # 숫자 받으면서 n(가장 큰 값)의 인덱스 저장
    for i in range(n):
        tmp = int(input())
        if tmp == n:
            max_num_idx = i
        nums.append(tmp)

    # max_num 이후로 내림차순인지 확인 -> 아니면 NO
    if nums[max_num_idx:] != sorted(nums[max_num_idx:], reverse=True):
        print('NO')
    else:
        result = ['+']*(nums[0]) + ['-']
        # 체크했는지 여부 표시하는 배열 check
        check = [0] * (n + 1)
        # 가장 최근에 체크한 수 now
        now = nums[0]
        check[nums[0]] = 1
        # NO flag
        flag = 0
        # 체크한 수 중 가장 큰 수
        tmp_max = nums[0]
        for i in range(1, n):
            # 현재 수가 now보다 작을 때
            if nums[i] < now:
                gap = now-nums[i]
                # gap이 1 보다 크면 그 사이에 체크한 수 확인
                if gap > 1:
                    if check[nums[i]:now].count(1) != gap-1:
                        flag = 1
                        print('NO')
                        break
                result.append('-')
            # 현재 수가 now보다 클 때: 이제껏 나온 수 중 가장 큰 수에서 뺀 만큼 + 더하기
            else:
                gap = nums[i]-tmp_max
                result.extend('+'*gap)
                result.append('-')
            check[nums[i]] = 1
            now = nums[i]
            tmp_max = max(tmp_max, now)

        if not flag:
            for r in result:
                print(r)