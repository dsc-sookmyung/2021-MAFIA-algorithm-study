# 프로그래머스 기능개발.py
# 작업의 진도 : progresses 개발 속도 : speeds
# return: 각 배포마다 몇개의 기능이 배포되는가

def solution(progresses, speeds):
    progresses = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    answer = []
    maximum=progresses[0]
    touch=0
    count=0
    print(progresses)

    for i in range(len(progresses)):
        if(progresses[i]>maximum):
            answer.append(count)
            count=1
            maximum=progresses[i]
        else:
            count+=1
        if(i==len(progresses)-1):
            answer.append(count)
    return answer
