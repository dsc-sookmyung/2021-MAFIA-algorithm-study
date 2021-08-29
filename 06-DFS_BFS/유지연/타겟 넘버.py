# 데이터가 그래프 형태로 이루어져 있고, 그래프 끝에 노드까지 가서 그 값을 더하거나 뺀 값 얻어야함 -> DFS

# Solution1 : DFS - 반복

def iterative_solution(numbers, target):
    result_list = [0]

    for i in range(len(numbers)):
        temp_list = []

        for j in range(len(result_list)):
            temp_list.append(result_list[j] - numbers[i])
            temp_list.append(result_list[j] + numbers[i])
        result_list = temp_list
        print(result_list)

    return result_list.count(target)




# Solution2 : DFS - 재귀

def solution(numbers, target):
    cnt = 0

    def operator(numbers, target, idx=0):
        if idx < len(numbers):
            numbers[idx] *= 1
            operator(numbers, target, idx+1)

            numbers[idx] *= -1
            operator(numbers, target, idx+1)

        elif sum(numbers) == target:
            nonlocal cnt
            cnt += 1

    operator(numbers, target)

    return cnt

# 공간 복잡도 개선 

def solution(numbers, target):
    cnt = 0
    len_numbers = len(numbers)

    def operator(idx=0):
        if idx < len_numbers:
            numbers[idx] *= 1
            operator(idx+1)

            numbers[idx] *= -1
            operator(idx+1)

        elif sum(numbers) == target:
            nonlocal cnt
            cnt += 1

    operator()

    return cnt


# 참고한 블로그1 : https://sexy-developer.tistory.com/40
# 참고한 블로그2 :https://itholic.github.io/kata-target-number/