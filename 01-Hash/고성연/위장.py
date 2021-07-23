def solution(clothes):
    answer = 1
    dic = {}
    for item in clothes:
        if item[1] in dic:
            dic[item[1]] += 1
        else:
            dic[item[1]] = 1
    for value in dic.values():
        answer *= value+1
    answer -= 1
    return answer
