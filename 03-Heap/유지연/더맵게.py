# Solution 1
def solution(scoville, K):
    arr = scoville
    count = 0

    while(min(arr)<K):
        m1 = min(arr)
        arr.remove(m1)
        m2 = min(arr)
        arr.remove(m2)
        n = m1 + m2 * 2
        arr.append(n)
        count +=1
    
    return count
# 생각나는대로 푼 방법 정확도 테스트 몇개와 효율성 테스트를 통과하지 못했다.
# 최소값를 heap이 아닌 min을 사용하였다.




# Solution 2
import heapq

def solution(scoville, k):
    heap = []
    for num in scoville :
        heapq.heappush(heap, num)

        mix_cnt = 0
    while heap[0] < k :
        try :
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        except IndexError:
            return -1
        mix_cnt += 1

    return mix_cnt


# heap을 이용한 풀이 -> 직접 최소 힙을 구현하지 않아도 되는 장점
# heapq는 일반적인 리스트와 다르게, 가지고 있는 요소를 push, pop 할때마다 자동으로 정렬해준다. 
# sort와 달리 heapq는 전체를 정렬하는 것이 아니다. 가장 작은 값을 가지는 원소를 리스트 맨 앞에 정렬한다. -> 최소값을 뽑을때 두번째 작은 원소 heap[1]이 아닌 heapq.heappop(heap)
# heapq 모듈 이해하는데 참고한 블로그 : https://www.daleseo.com/python-heapq/