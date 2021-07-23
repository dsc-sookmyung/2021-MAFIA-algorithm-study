
def solution(participant, completion):
    d = dict()
    hashValue = 0
    for p in participant:
        d[hash(p)] = p
        hashValue += hash(p)
    for c in completion:
        hashValue -= hash(c)
    return d[hashValue]

"""
처음에 하나의 for문으로 풀었는데 동명이인 고려가 안됨
이중 for문으로 풀었더니 시간초과가 발생하였음
hash라는 주제를 통해 구글링해보면서 풀었음 -> hash를 이론으로만 알고 있어서 다시 공부해야한다 ^^
"""