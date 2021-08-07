def solution(array, commands):
    answer = []
    for command in commands:
        sliced = array[command[0]-1:command[1]]
        sliced.sort()
        answer.append(sliced[command[2]-1])
    return answer
