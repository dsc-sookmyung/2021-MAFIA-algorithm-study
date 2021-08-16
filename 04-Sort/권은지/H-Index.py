def solution(citations):
    citations.sort()
    answer = len(citations)
    for i in range(answer):
        if citations[i] >= answer-i:
            return answer-i
    return 0