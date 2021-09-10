def solution(brown, yellow):
    total = brown+yellow
    for row in range(3, total+1):
        col = total//row
        if row*col == total and row >= col and (row-2)*(col-2) == yellow:
            answer = [row, col]
            return answer