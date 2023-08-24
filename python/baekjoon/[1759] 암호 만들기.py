# https://www.acmicpc.net/problem/1759
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def dfs(pw, cnt, ja, mo):
    if len(pw) == L and ja >= 2 and mo >= 1:
        print(pw)
        return
    elif cnt == C: return
    if arr[cnt] in 'aeiou':
        dfs(pw+arr[cnt], cnt+1, ja, mo+1)
    else:
        dfs(pw+arr[cnt], cnt+1, ja+1, mo)
    dfs(pw, cnt+1, ja, mo)

L, C = map(int, input().split())
arr = sorted(list(input().split()))
dfs('', 0, 0, 0)