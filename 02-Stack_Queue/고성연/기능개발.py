def solution(progresses, speeds):
    answer = []
    while len(progresses) > 0:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        count = 0
        while progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
            if not progresses:
                break
        if count > 0:
            answer.append(count)

    return answer
