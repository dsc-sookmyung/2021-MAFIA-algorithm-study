# Solution 1
def solution(numbers):
	#answer = []
	answer = list(map(str, numbers))
	answer.sort(reverse=True)
	print(answer)
	word = "".join(answer)
	#print(word)
	return word

# 실패
# 숫자가 아니라 아스키코드로 비교하면 된다고 생각은 했으나 한자리, 두자리, 세자리 수 크기 비교가 안되고 9534303 결과가 나옴



# Solution 2
from itertools import permutations

def solution(numbers):
    result = list(permutations(numbers,len(numbers)))
	# print(result)
	"""
	for i in result:
		print (i) # (6, 10, 2) -> 리스트안 튜플 하나씩 꺼냄
		word = ''.join(map(str,i))
		print(word) # 6102 -> 튜플에서 값을 문자열로 바꿈
	"""
	result2 = [''.join(map(str,i)) for i in result]
	answer = max(result2)
	
	return answer
    
# 실패
# 시간초과때문에 처음에 고려를 안했던 방법이지만 혹시나 했더니 역시나였다. -> permutations 사용
# 이해가 안되는 부분을 for문으로 풀어서 썼는데 이건 항상 헷갈렸던 부분이니 계속 봐야할것 같다.
# map(function, iterable)



# Solution 3
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: x*3, reverse=True)
    
    return str(int(''.join(numbers)))

# numbers 배열을 str으로 변환하게끔 매핑하여 배열로 리턴함
# lambda x : x*3은 numbers 인자 각각의 문자열을 3번 반복하여 numbers 인수값이 1000이하이므로 3자리수로 맞추고 비교하는 것 -> 문자열이라 아스키로 비교
# sort는 기본 오름 차순
# join만 사용하면 0일 때가 문제라서 str로 반환하라고 했다고 함
# 참고한 블로그 : https://hocheon.tistory.com/48
