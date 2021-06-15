def solution(X, Y, D):
    result = (Y-X)//D
    result = result if not (Y-X)%D else result+1
    return result