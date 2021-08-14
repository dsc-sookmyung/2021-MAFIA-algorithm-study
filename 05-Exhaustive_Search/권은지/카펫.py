import math

def solution(brown, yellow):
    div = []
    for i in range(1, int(math.sqrt(yellow) + 1)): # sqrt 안하고 yellow/2로 하면 같은 수의 조합인데 순서만 앞뒤로 바뀌어서 나옴
        if yellow % i == 0:
            div.append([yellow/i, i])

    answer = []

    for j in range(len(div)):
        width = int(div[j][0])
        length = int(div[j][1])
        if 4 + (width * 2) + (length * 2) == brown:
            answer.append(int(div[j][0]) + 2)
            answer.append(int(div[j][1]) + 2)

    return answer