# Solution1
def solution(priorities, location):
    answer = 0

    array1 = [c for c in range(len(priorities))] # index 위치 저장 
    array2 = priorities.copy() # 값 저장 (출력되는 값)

    i = 0
    while True:
        if array2[i] < max(array2[i+1:]):
            array1.append(array1.pop(i))
            array2.append(array2.pop(i))
        else:
            i += 1

        if array2 == sorted(array2, reverse=True):
            break

    return array1.index(location) + 1

# 중요도가 같은 경우도 생각해야함



# Solution2
def solution(priorities, location):
    answer = 0
    from collections import deque

    d = deque([(v,i) for i,v in enumerate(priorities)])

    while len(d):
        item = d.popleft()
        if d and max(d)[0] > item[0]:
            d.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer

# deque 이용, 시간이 빠르다.
# 참고한 블로그 : https://eda-ai-lab.tistory.com/461



# Solution3
def solution(priorities, location):
    answer = 0
    m = max(priorities)
    while True:
        v = priorities.pop(0)
        if m == v:
            answer += 1
            if location == 0:
                break
            else:
                location -= 1
            m = max(priorities)
        else:
            priorities.append(v)
            if location == 0:
                location = len(priorities)-1
            else:
                location -= 1
    return answer

# 추가 리스트를 선언하지 않고 location값을 하나씩 빼고, answer 값을 추가해가면서 답에 접근하는 방식