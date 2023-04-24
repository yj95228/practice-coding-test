# https://programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    answer = []
    for i in reversed(range(len(list(str(n))))):
        answer.append(int(list(str(n))[i]))
    return answer
