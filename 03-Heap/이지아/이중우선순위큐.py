# 프로그래머스 더 맵게.py
# break는 실패 >> pass 사용(차이점 정리) 
# heapq 모듈 nlargest(n, list), nsamllest(n, list) 

import heapq

def solution(operations):
    answer = []
    for operation in operations:
        a,b=operation.split(" ")
        if a=="I":
            heapq.heappush(answer,int(b))
        else:
            if len(answer)>0:
                if b=="1":
                    answer.pop(answer.index(heapq.nlargest(1,answer)[0]))
                else:
                    heapq.heappop(answer)
            else:
                pass
    if len(answer) ==0:
        return [0,0]
    else:
        return [heapq.nlargest(1,answer)[0], heapq.nsmallest(1,answer)[0]]
