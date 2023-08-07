# https://www.acmicpc.net/problem/15650
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