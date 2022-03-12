# https://programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    answer = []
    a = 0
    b = 0
    for i in range(1, min(n, m) + 1):
        if (n % i == 0) and (m % i == 0):
            a = i
    b = n * m / a
    answer = [a, b]
    return answer
