# https://www.acmicpc.net/problem/10819
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def dfs(arr, sm, last):
    global answer
    if len(arr) == N:
        if answer < sm: answer = sm
    else:
        for i, x in enumerate(lst):
            if arr:
                if i not in arr:
                    dfs(arr+[i], sm+abs(last-x), x)
            else:
                dfs(arr+[i], sm, x)
N = int(input())
lst = list(map(int, input().split()))
answer = 0
dfs([],0,None)
print(answer)