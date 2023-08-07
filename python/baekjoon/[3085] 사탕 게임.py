# https://www.acmicpc.net/problem/3085
import sys

def count(lst):
    result = cnt = 1
    for i in range(1,N):
        if lst[i] == lst[i-1] and lst[i] != 0:
            cnt += 1
            result = max(cnt, result)
        else:
            cnt = 1
    return result

def solve(arr):
    result = 0
    for i in range(N):
        result = max(result, count(arr[i]))
        for j in range(N):
            # 아래쪽과 바꾸는 경우
            if i < N-1:
                arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
                result = max(result, count(arr[i]), count(arr[i+1]))
                arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            # 오른쪽과 바꾸는 경우
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            result = max(result, count(arr[i]))
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
    return result

sys.stdin = open('input.txt','r')
input = sys.stdin.readline
N = int(input())
matrix = [list(input().strip())+[0] for _ in range(N)] + [[0]*(N+1)]
t_matrix = list(map(list, zip(*matrix)))
answer = max(solve(matrix), solve(t_matrix))
print(answer)