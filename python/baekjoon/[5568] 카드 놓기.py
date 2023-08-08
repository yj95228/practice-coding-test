# https://www.acmicpc.net/problem/5568
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def dfs(arr, result):
    if len(arr) == K:
        s.add(''.join(result))
    else:
        for i,x in enumerate(lst):
            if not arr or i not in arr:
                dfs(arr+[i], result+[x])
N = int(input())
K = int(input())
lst = [input().strip() for _ in range(N)]
s = set()
dfs([], [])
print(len(s))