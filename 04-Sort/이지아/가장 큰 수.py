import functools

def comparator(x,y):
    method1 = x+y
    method2 = y+x
    return (int(method1) > int(method2)) - (int(method1) < int(method2)) 

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer

"""

생각해 봐야 할 점: 시간이 오래 걸림 
테스트 1 〉	통과 (1439.00ms, 21.7MB)
테스트 2 〉	통과 (593.67ms, 16.5MB)
테스트 3 〉	통과 (2228.19ms, 25.2MB)
테스트 4 〉	통과 (14.98ms, 10.5MB)
테스트 5 〉	통과 (1203.28ms, 20.5MB)
테스트 6 〉	통과 (977.74ms, 19MB)
테스트 7 〉	통과 (0.07ms, 10.3MB)
테스트 8 〉	통과 (0.05ms, 10.3MB)
테스트 9 〉	통과 (0.06ms, 10.4MB)
테스트 10 〉	통과 (0.05ms, 10.3MB)
테스트 11 〉	통과 (0.09ms, 10.4MB)

배운 내용: functools.cmp_to_key(comparator)

"""
