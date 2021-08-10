def solution(citations):
    answer = 0
    citations.sort()
    n = len(citations)
    for i in range(n):
        if citations[i] >= n-i:
            answer = n-i
            break
    return answer
