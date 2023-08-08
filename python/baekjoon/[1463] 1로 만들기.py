# https://www.acmicpc.net/problem/18290
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def dfs(x, cnt):
    global answer
    if cnt > answer: return
    if x == 1:
        answer = min(answer, cnt)
        return
    if x%3 == 0: dfs(x//3, cnt+1)
    if x%2 == 0: dfs(x//2, cnt+1)
    dfs(x-1, cnt+1)
N = int(input())
answer = pow(10,6)
dfs(N,0)
print(answer)