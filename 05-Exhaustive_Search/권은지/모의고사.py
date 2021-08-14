def solution(answers):
    answer = []

    mh1 = [1, 2, 3, 4, 5]
    mh2 = [2, 1, 2, 3, 2, 4, 2, 5]
    mh3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    count = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i] == mh1[i % len(mh1)]:
            count[0] += 1
        if answers[i] == mh2[i % len(mh2)]:
            count[1] += 1
        if answers[i] == mh3[i % len(mh3)]:
            count[2] += 1

    for j in range(3):
        if count[j] == max(count):
            answer.append(j + 1)

    return answer