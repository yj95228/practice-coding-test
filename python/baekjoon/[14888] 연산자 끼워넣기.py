# https://www.acmicpc.net/problem/14888
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def dfs(n, result):
    global min_answer, max_answer
    if n == N-1:
        min_answer = min(result, min_answer)
        max_answer = max(result, max_answer)
        return
    plus, minus, multiple, divide = math_arr
    if plus:
        math_arr[0] -= 1
        dfs(n+1, result+arr[n+1])
        math_arr[0] += 1
    if minus:
        math_arr[1] -= 1
        dfs(n+1, result-arr[n+1])
        math_arr[1] += 1
    if multiple:
        math_arr[2] -= 1
        dfs(n+1, result*arr[n+1])
        math_arr[2] += 1
    if divide:
        math_arr[3] -= 1
        dfs(n+1, result//arr[n+1] if result > 0 else -(-result//arr[n+1]))
        math_arr[3] += 1

N = int(input())
arr = list(map(int, input().split()))
math_arr = list(map(int, input().split()))
# FIXME: max_answer 초기화를 음수로 두지 않고 0으로 뒀었음
# 초기값을 정해두지 않고 결과값들을 array로 받고 min, max 출력하는 방법도 가능할듯
min_answer, max_answer = 10_000_000_000, -10_000_000_000
dfs(0,arr[0])
print(max_answer)
print(min_answer)