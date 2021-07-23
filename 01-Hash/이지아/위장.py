def solution(clothes):
    answer=1
    style={}
    #val = 의상의 이름, key = 종류(의상 타입)
    for val, key in clothes:
        if key in style.keys():
            style[key].append(val)
        else:
            style[key] = [val]

    for val in style.values():
        answer *= (len(val) + 1)

    answer= answer-1

    return answer
