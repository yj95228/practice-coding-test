# https://www.acmicpc.net/problem/15649
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