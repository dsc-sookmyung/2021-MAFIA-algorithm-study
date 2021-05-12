def solution(clothes):
    answer = 1
    closet = {}
    for element in clothes:
        key = element[1]
        value = element[0]
        if key in closet:
            closet[key].append(value)
        else:
            closet[key] = [value]

    for key in closet.keys():
        answer = answer * (len(closet[key]) + 1)
    return answer - 1