def solution(answers):
    answer = []

    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    scores = [0, 0, 0]

    for i in range(len(answers)):
        if supo1[i % len(supo1)] == answers[i]:
            scores[0] += 1
        if supo2[i % len(supo2)] == answers[i]:
            scores[1] += 1
        if supo3[i % len(supo3)] == answers[i]:
            scores[2] += 1

    for idx, score in enumerate(scores):
        if score == max(scores):
            answer.append(idx + 1)

    return answer
