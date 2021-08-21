def solution(answers):
    arr1 = [1,2,3,4,5]
    arr2 = [2,1,2,3,2,4,2,5]
    arr3 = [3,3,1,1,2,2,4,4,5,5]
    num1, num2, num3 = 0, 0, 0
    answer = []

    for i in range(len(answers)):
        if arr1[i%5] == answers[i]:
            num1 = num1 + 1
        if arr2[i%8] == answers[i]:
            num2 = num2 + 1
        if arr3[i%10] == answers[i]:
            num3 = num3 + 1

    if max(num1,num2,num3) == num1:
        answer.append(1)
    if max(num1,num2,num3) == num2:
        answer.append(2)
    if max(num1,num2,num3) == num3:
        answer.append(3)

    return answer

# 성공
# 길이에 따라 반복되는 리스트를 나머지 개념을 이용하여 풀었다. 