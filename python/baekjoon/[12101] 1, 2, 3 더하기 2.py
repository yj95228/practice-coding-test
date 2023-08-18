# https://www.acmicpc.net/problem/12101
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def dfs(arr):
    if sum(arr) == N:
        answer.append(arr)
        return
    elif sum(arr) > N:
        return
    for x in [1,2,3]:
        dfs(arr+[x])

N, K = map(int, input().split())
answer = []
dfs([])
try: print('+'.join(map(str,answer[K-1])))
except: print(-1)