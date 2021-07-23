def solution(phone_book):
    answer = True
    hashmap = {}
    for phone_number in phone_book:
        hashmap[phone_number] = 1 #key-value 쌍 
    for phone_number in phone_book:
        temp = "" #temp초기화
        for number in phone_number:
            temp += number
            if temp in hashmap and temp != phone_number:
                return False
    return True

