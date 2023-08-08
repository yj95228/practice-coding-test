# https://www.acmicpc.net/problem/9663
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def dfs(arr):
    global answer
    if len(arr) == N:
        answer += 1
    else:
        for x in range(N):
            if arr:
                for i in range(1,len(arr)+1):
                    if arr[-i] in (x-i,x,x+i): break
                else:
                    dfs(arr+[x])
            else:
                dfs(arr+[x])

N = int(input())
answer = 0
dfs([])
print(answer)