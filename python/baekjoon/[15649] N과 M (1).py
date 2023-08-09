# https://www.acmicpc.net/problem/15649
# N개 중 M개 순열
import sys

def dfs(arr):
    if len(arr) == M:
        print(*arr)
        return
    for i in range(1,N+1):
        if not arr or i not in arr:
            dfs(arr+[i])

sys.stdin = open('input.txt','r')
input = sys.stdin.readline
N, M = map(int, input().split())
dfs([])

# 강사님 코드
def dfs(n, arr):
    if n == M:            # 종료조건
        print(*arr)
        return 0

    for j in range(1, N+1):
        if not visited[j]:
            visited[j] = True
            dfs(n+1, arr+[j])
            visited[j] = False      # 잊지마세요!


N, M = map(int, input().split())
visited = [False]*(N+1)
ansswer = dfs(0, [])