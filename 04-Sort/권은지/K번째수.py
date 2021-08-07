def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        start = commands[i][0]
        end = commands[i][1]
        cut = array[start-1:end]
        cut.sort()
        place = commands[i][2]
        num = cut[place-1]
        answer.append(num)
    return answer