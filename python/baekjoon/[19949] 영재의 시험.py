# https://www.acmicpc.net/problem/19949
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def dfs(arr, cnt, score):
    global answer
    if cnt >= 6 and score <= cnt-6: return
    if cnt == 10:
        answer += 1
        return
    for x in range(1,6):
        if cnt < 2 or (cnt >= 2 and not (x == arr[-1] and x == arr[-2])):
            dfs(arr+[x], cnt+1, score+1 if x == lst[cnt] else score)

lst = list(map(int, input().split()))
answer = 0
dfs([],0,0)
print(answer)