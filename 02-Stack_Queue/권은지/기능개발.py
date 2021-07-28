def solution(progresses, speeds):
    ends = []
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] == 0:
            count = (100 - progresses[i]) // speeds[i]
            ends.append(count)

        else:
            count = ((100 - progresses[i]) // speeds[i]) + 1
            ends.append(count)

    num = 0
    answer = []
    for j in range(len(ends)):
        if j == 0:
            answer.insert(0, 1)
        elif ends[j-1] >= ends[j]:
            answer[num] = answer[num] + 1

        else:
            num = num + 1
            answer.insert(num, 1)

    return answer