# 프로그래머스 주식가격.py
# prices: 초 단위로 기록된 주식가격 배열 
# return: 가격이 떨어지지 않은 기간은 몇 초인지

#brute-force 
def solution(prices):
    answer =[0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i]+=1
            else:
                answer[i]+=1
                break
    return answer
