def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(len(prices)-i-1):
            answer[i] += 1
            if prices[i] <= prices[j+i+1]:
                continue
            else:
                break
    return answer