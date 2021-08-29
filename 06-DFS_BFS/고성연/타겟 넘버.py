def solution(numbers, target):
    answer = 0
    parents = [0]
    for num in numbers:
        child = []
        for parent in parents:
            child.append(parent + num)
            child.append(parent - num)
        parents = child

    for result in parents:
        if result == target:
            answer += 1

    return answer
