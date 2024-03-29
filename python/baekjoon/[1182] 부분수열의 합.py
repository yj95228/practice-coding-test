# https://www.acmicpc.net/problem/1182
# N개 중 0~N개 조합 모든 경우 (부분집합, powerset)
import sys

def dfs(arr):
    global answer
    if len(arr) > N: return
    if arr and sum([x[1] for x in arr]) == S:
        answer += 1
    for i, x in enumerate(lst):
        if not arr or arr[-1][0] < i:
            dfs(arr+[(i,x)])

sys.stdin = open('input.txt','r')
input = sys.stdin.readline
N, S = map(int, input().split())
lst = list(map(int, input().split()))
answer = 0
dfs([])
print(answer)

# 강사님 코드
def dfs(n, sm, cnt):
    global answer
    if n == N:
        if sm == S and cnt > 0:
            answer += 1
            return
    dfs(n+1, sm, cnt)   # 포함X
    dfs(n+1, sm+lst[n], cnt+1)   # 포함O

# 비트마스킹
answer = 0
for bits in range(1, 2**N): # 1 << N
    sm = 0
    for pos in range(N):
        if bits & (1<<pos):
            sm += lst[pos]
    if sm == S: answer += 1
print(answer)