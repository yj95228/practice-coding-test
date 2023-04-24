# https://programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    answer = 0
    newn = list(str(n))
    newnn = sorted(newn, reverse = True)
    answer = int("".join(newnn))
    return answer
