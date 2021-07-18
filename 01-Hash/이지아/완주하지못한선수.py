def solution(participant, completion):
    participant.sort()
    completion.sort()
    com = len(completion)

    for i in range(com) :
        if participant[i] != completion[i] : 
            return participant[i]
    return participant[com]
