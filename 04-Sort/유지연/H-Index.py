# Solution 1
def solution(citations):
    answer = 0
    temp = sorted(citations)
    n = len(temp)
    for i in range(n):
        if (temp[i]>=(n-i)):
            answer = temp[i]
        
    return answer

# 실패
# 이유는 확실히는 모르겠음.. 0의 경우 예외처리를 안해줘서 그런가 의문..



# Solution 2
def solution(citations):
    # answer = 0
    citations.sort()
    # print(citations)
    n = len(citations)
    for i in range(n):
        if citations[i] >= (n-i):
            return n-i
    return 0

# 성공
# 위의 풀이와 달리 논문이 인용된 횟수(h번 이상) >= 인용된 논문의 개수(h개 == h번) 이므로 부등호 방향을 바꾸었음
# answer라는 변수대신 상황에 따라 리턴값을 설정