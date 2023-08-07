# https://www.acmicpc.net/problem/15654
import sys

def dfs(arr):
    if len(arr) == M:
        print(*arr)
    else:
        for x in lst:
            if not arr or x not in arr:
                dfs(arr+[x])
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
dfs([])