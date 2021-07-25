# 프로그래머스 다리를 지나는 트럭(python)
# bridge_length: 다리의 길이, weight: 하중 견디는 최대 무게, truck_weights: 트럭들의 무게(배열)
# return: 모든 트럭이 다리를 지나가는데 걸리는 시간 


#queue 사용
def solution(bridge_length, weight, truck_weights):
    time = 0
    queue=[0]*bridge_length
    
    while queue:
        time+=1
        queue.pop(0)
        if truck_weights:
            if sum(queue)+truck_weights[0]<=weight:
                queue.append(truck_weights.pop(0))
            else:
                queue.append(0)
        
    return time
