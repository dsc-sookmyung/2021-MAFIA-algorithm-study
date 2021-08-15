def solution(brown, yellow):
    xy = brown + yellow

    for y in range(1, xy+1):
        if (xy % y) == 0:
            x = xy // y
            if (x-2)*(y-2) == yellow:
                answer = [x, y]
                break

    return answer
