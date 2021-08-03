# Solution 1
def solution(array, commands):
    answer = []
	
    for num in range(len(commands)):
        i = commands[num][0]
        j = commands[num][1]
        k = commands[num][2]
        temp = array
        temp = sorted(temp[i-1:j])
        #print(temp)
        answer.append(temp[k-1])

    return answer

# 리스트 슬라이싱시 인덱스값 주의 : 처음 포함 마지막 불포함
# print(temp[i-1:j].sort()) 하면 None 나옴
# sort 함수는 리스트명.sort( ) 형식으로 "리스트형의 메소드"​​이며 리스트 원본값을 직접 수정한다. -> 리턴값이 None이다. 단지 원본 리스트값이 수정될 뿐
# sorted 함수는 sorted( 리스트명 ) 형식으로 "내장 함수"이며 리스트 원본 값은 그대로이고 정렬 값을 반환한다. 



# Solution 2
def solution(array, commands):
    answer = []
    for command in commands:
        new_array = array[command[0]-1:command[1]]
        new_array.sort()
        answer.append(new_array[command[2]-1])
    
    return answer

# 위에 풀이와 달리 굳이 하나씩 숫자를 지정해주시 않고 바로 지정하여 쓸 수 있다. 코드가 훨씬 간결하다. 