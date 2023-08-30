# https://www.acmicpc.net/problem/15664
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def dfs(arr):
    if len(arr) == M:
        ss.add(tuple(map(lambda x: lst[x], arr)))
        return
    for x in range(N):
        if not arr or arr[-1] < x:
            dfs(arr+[x])

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
ss = set()
dfs([])
for s in ss:
    print(*s)