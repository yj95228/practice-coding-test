# https://www.acmicpc.net/problem/15651
import sys

def dfs(arr):
    if len(arr) == M:
        print(*arr)
    else:
        for i in range(1,N+1):
            dfs(arr+[i])

sys.stdin = open('input.txt', 'rt')
input = sys.stdin.readline

N, M = map(int, input().split())
dfs([])