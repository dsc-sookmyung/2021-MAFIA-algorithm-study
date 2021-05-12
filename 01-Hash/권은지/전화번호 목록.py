def solution(phone_book):
    answer = True
    phone_book.sort()
    for x,y in zip(phone_book, phone_book[1:]):
        if y.startswith(x):
            answer = False
            break
    return answer