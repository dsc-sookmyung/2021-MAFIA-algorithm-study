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
