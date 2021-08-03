# 프로그래머스 더 맵게.py
# scoville: 음식의 스코빌 지수를 담은 배열 k: 최소 지수 
# return: 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수
# 정확성: 76.2, 효율성: 23.8, 합계: 100.0 / 100.0

import heapq

def solution(scoville, k):
    heapq.heapify(scoville)
    result = 0
    while scoville[0] < k:
        if len(scoville) > 1:
            heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
            result += 1
        else:
            return -1
    return result
  
