# https://programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    answer = []
    a = arr[0]
    b = 0
    for i in range(len(arr)):
        if arr[i] < a:
            a = arr[i]
            b = i
    arr.pop(b)
    if arr == []:
        return [-1]
    else:
        answer = arr
    return answer
