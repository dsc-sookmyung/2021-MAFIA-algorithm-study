from collections import deque


def solution(priorities, location):
    answer = 0
    index_queue = deque(range(len(priorities)))
    priorities_queue = deque(priorities)
    while True:
        max_priorities = max(priorities_queue)
        priorities_head = priorities_queue.popleft()
        index_head = index_queue.popleft()
        if priorities_head == max_priorities:
            answer += 1
            if index_head == location:
                break
        else:
            priorities_queue.append(priorities_head)
            index_queue.append(index_head)

    return answer

