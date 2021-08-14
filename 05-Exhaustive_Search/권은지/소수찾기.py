from itertools import permutations

def prime_number(num):
    if num == 0 or num == 1:
        return False
    else:
        for i in range(2, int(num/2 + 1)):
            if num % i == 0:
                return False
        return True

def solution(numbers):
    answer = []

    for i in range(1, len(numbers) + 1):
        arr = list(permutations(numbers, i))
        for j in range(len(arr)):
            num = int(''.join(map(str, arr[j])))
            if prime_number(num):
                answer.append(num)

    answer = list(set(answer)) # 겹치는 숫자가 있는걸 방지

    return len(answer)

# permutations(n, m)
# permutations = 순열
# n에 있는 객체들 중 m만큼 뽑아서 만듬
# 중복 허용 X
# 순서에 의미가 있음 (같은 값이더라도 순서가 다르면 다른 값으로 판단)

# print(list(permutations([1,2,3,4], 2)))
# [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]