from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0]*bridge_length)
    truck_queue = deque(truck_weights)
    bridge_sum = 0
    while bridge:
        answer += 1
        bridge_sum -= bridge.popleft()
        if truck_queue:
            if (bridge_sum + truck_queue[0]) <= weight:
                bridge_sum += truck_queue[0]
                bridge.append(truck_queue.popleft())
            else:
                bridge.append(0)

    return answer
