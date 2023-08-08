# https://www.acmicpc.net/problem/10974
import sys

def dfs(arr):
    if len(arr) == N:
        print(*arr)
    else:
        for x in range(1,N+1):
            if not arr or x not in arr:
                dfs(arr+[x])

sys.stdin = open('input.txt','r')
input = sys.stdin.readline
N = int(input())
dfs([])