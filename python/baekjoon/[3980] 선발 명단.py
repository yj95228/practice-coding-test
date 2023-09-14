# https://www.acmicpc.net/problem/3980
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def recur(n, result):
    global answer
    if n == 11:
        answer = max(answer, result)
        return
    for i in range(11):
        if not visited[i] and matrix[n][i]:
            visited[i] = True
            recur(n+1, result+matrix[n][i])
            visited[i] = False

T = int(input())
for _ in range(T):
    matrix = [list(map(int, input().split())) for _ in range(11)]
    visited = [False]*11
    answer = 0
    recur(0, 0)
    print(answer)