# https://www.acmicpc.net/problem/15650
# N개 중 M개 조합
import sys

def dfs(arr):
    if len(arr) == M:
        print(*arr)
        return
    for i in range(1,N+1):
        if not arr or arr[-1] < i:
            dfs(arr+[i])

sys.stdin = open('input.txt','r')
input = sys.stdin.readline
N, M = map(int, input().split())
dfs([])

# 강사님 코드
def dfs(n, start, arr):
    if n == M:
        print(*arr)
        return
    for j in range(start,N+1):
        dfs(n+1, j+1, arr+[j])
answer = dfs(0, 1, [])