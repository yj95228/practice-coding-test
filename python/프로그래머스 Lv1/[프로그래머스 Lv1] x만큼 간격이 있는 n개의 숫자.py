# https://programmers.co.kr/learn/courses/30/lessons/12954

def solution(x, n):
    answer = []
    y = x
    while n > 0:
        answer.append(y)
        n -= 1
        y += x
    return answer
