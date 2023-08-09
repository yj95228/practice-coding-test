# https://www.acmicpc.net/problem/15663
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def dfs(arr):
   if len(arr) == M:
       print(*arr)
       return
   for x in sorted(counts.keys()):
       if counts.get(x):
           counts[x] -= 1
           dfs(arr+[x])
           counts[x] += 1

N, M = map(int, input().split())
lst = list(map(int, input().split()))
counts = dict()
for x in lst:
    counts[x] = counts.get(x, 0) + 1
dfs([])