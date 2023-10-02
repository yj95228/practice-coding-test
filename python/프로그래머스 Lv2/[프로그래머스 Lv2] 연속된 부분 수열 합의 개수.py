# https://school.programmers.co.kr/learn/courses/30/lessons/131701
def solution(elements):
    answer = set()
    N = len(elements)
    elements += elements
    for n in range(N):
        for i in range(N):
            answer.add(sum(elements[i:i+n]))
    return len(answer)