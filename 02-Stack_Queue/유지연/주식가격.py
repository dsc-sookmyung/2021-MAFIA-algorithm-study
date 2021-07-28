# Solution 1
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

# 처음에 이렇게 생각. 그러나 시간 효율이 떨어짐



# Solution 2
def solution(prices):
    # answer = 몇초 후 가격이 떨어지는지 저장하는 배열
    answer = [len(prices)-i-1 for i in range(len(prices))]
    
    # stack = prices의 인덱스를 차례로 담아두는 배열
    stack = [0]
    
    for i in range(1, len(prices)):
        while stack:
            index = stack[-1]
            
            # 주식 가격이 떨어졌다면
            if prices[index] > prices[i]:
                answer[index] = i - index
                stack.pop()
            
            # 떨어지지 않았다면 다음 시점으로 넘어감 (주식 가격이 계속 증가하고 있다는 말)
            else:
                break
        
        # 스택에 추가한다.
        # 다음 시점으로 넘어갔을 때 다시 비교 대상이 될 예정이다.
        stack.append(i)
        
    return answer

# 위의 방법 대비 시간 효율이 좋음, 시간의  흐름대로 반복문을 진행하면서 현재 시점보다 가격이 높은 시점이 언제였는지 판단하는 방식
# 참고한 블로그 : https://tngusmiso.tistory.com/34



# Solution3
def solution(prices):
    answer = [0]*len(prices)
    stack = []
 
    for i, price in enumerate(prices):
        #stack이 비었이면 false
        while stack and price < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
 
    # for문 다 돌고 Stack에 남아있는 값들 pop
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j
 
    return answer

# 처음 price를 stack에 쌓고 다음 price가 더 크면 스택에 쌓고 작으면 pop을 한다. 
# 참고한 블로그 : https://deftkang.tistory.com/175
# enumerate -> 리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능을 가집니다. 순서가 있는 자료형(list, set, tuple, dictionary, string)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴합니다.