# TODO: 혼자 힘으로 다시 풀 수 있을지...
# https://www.acmicpc.net/problem/1799
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def dfs(n, cnt):
    global answer
    print(n, cnt, answer)
    # 남은 대각선에 모두 놓아도 갱신할 수 없는 경우
    if cnt + (diag-n) <= answer: return
    if n == diag:
        answer = max(answer, cnt)
        return
    for (r,c) in arr[n]:
        if not visited[r-c]:
            visited[r-c] = True
            dfs(n+1, cnt+1)
            visited[r-c] = False
    dfs(n+1, cnt)

N = int(input())
matrix = [list(input().split()) for _ in range(N)]
diag = N*2-1
arr = [[] for _ in range(diag)]
for i in range(N):
    for j in range(N):
        if matrix[i][j] == '1':
            arr[i+j].append((i,j))

visited = [False]*(2*N)
answer = 0
dfs(0,0)
print(answer)