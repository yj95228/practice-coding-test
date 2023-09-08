# https://www.acmicpc.net/problem/14501
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def dfs(day, money):
    global answer
    if day <= N: answer = max(answer, money)
    if day >= N: return
    dfs(day+1, money)
    dfs(day+arr[day][0], money+arr[day][1])

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0
dfs(0, 0)
print(answer)