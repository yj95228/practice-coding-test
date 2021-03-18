# https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(price):
    answer = [0]*len(price)
    for i in range(len(price)-1):
        for j in range(i+1, len(price)):
            answer[i] += 1
            if price[i] > price[j]:
                break
    return answer
