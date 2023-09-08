# https://www.acmicpc.net/problem/17626
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def dfs(sm, result):
    global answer
    if sm == 0:
        answer = min(answer, result)
        return
    elif sm < 0 or result >= answer-1:
        return
    for x in range(int(sm**(1/2)),0,-1):
        dfs(sm-x**2, result+1)

N = int(input())
answer = 4
dfs(N, 0)
print(answer)