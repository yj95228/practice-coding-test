# https://programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1, arr2):
    #answer = [[0]*len(arr1[0]) for i in range(len(arr1))]
    answer = [[0 for col in range(len(arr1[0]))] for row in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer
