# https://www.acmicpc.net/problem/15657
import sys

def dfs(arr):
    if len(arr) == M:
        print(*arr)
    else:
        for x in lst:
            if not arr or arr[-1] <= x:
                dfs(arr + [x])

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
dfs([])