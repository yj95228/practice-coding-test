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

# 강사님 코드
def dfs(n):
    global ans
    if n == N:
        ans += 1
        return

    for j in range(N):
        if not v1[j] and not v2[n+j] and not v3[n-j]:
            v1[j], v2[n+j], v3[n-j] = True, True, True
            dfs(n+1)
            v1[j], v2[n+j], v3[n-j] = False, False, False

N = int(input())
v1 = [False]*N
v2 = [False]*2*N
v3 = [False]*2*N

ans = 0
dfs(0)
print(ans)