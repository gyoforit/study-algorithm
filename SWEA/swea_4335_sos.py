import sys
sys.stdin = open('input_4335.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    boxes = []
    for _ in range(N):
        a, b, c = map(int, input().split())
        tmp = [a, b, c]
        tmp.sort(reverse=True)
        boxes.append(tmp)
    boxes.sort(reverse=True)
    # print(boxes)
    now_a, now_b = boxes[0][1], boxes[0][2]
    cnt = boxes[0][0]
    for b in range(1, N):
        if (now_a >= boxes[b][1] and now_b >= boxes[b][2]) or (now_a >= boxes[b][2] and now_b >= boxes[b][1]):
            cnt += boxes[b][0]
            now_a, now_b = boxes[b][1], boxes[b][2]

    print(cnt)