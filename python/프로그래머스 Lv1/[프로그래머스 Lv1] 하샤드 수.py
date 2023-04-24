# https://programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    answer = False
    newx = list(str(x))
    sum = 0
    for i in range(len(newx)):
        sum += int(newx[i])
    if x % sum == 0:
        answer = True
    return answer
