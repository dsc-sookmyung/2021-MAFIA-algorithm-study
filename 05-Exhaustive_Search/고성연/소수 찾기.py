from itertools import permutations


def is_prime_num(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def solution(numbers):
    prime_num = []

    for i in range(1, len(numbers)+1):
        temp_list = list(map(''.join, permutations(numbers, i)))
        for j in list(temp_list):
            if is_prime_num(int(j)):
                prime_num.append(int(j))

    answer = len(set(prime_num))

    return answer
