# https://www.acmicpc.net/problem/16938
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def dfs(idx, arr):
    global answer
    if sum(arr) > R: return
    if len(idx) >= 2 and L <= sum(arr) <= R and max(arr)-min(arr) >= X:
        answer += 1
    if len(idx) == N: return
    for i in range(N):
        if not idx or idx[-1] < i:
            dfs(idx+[i], arr+[lst[i]])

N, L, R, X = map(int, input().split())
lst = list(map(int, input().split()))
answer = 0
dfs([],[])
print(answer)

# 강사님 코드
def solve():
    for cnt in range(2,N+1):
        comb([0]*cnt, 0, 0, cnt, 0)
    print(answer)

def comb(arr, start, cnt, target, total):
    global answer
    if total > R: return
    if cnt == target:
        if total >= L and arr[target-1] - arr[0] >= X:
            answer += 1
        return
    for i in range(start, N):
        arr[cnt] = lst[i]
        comb(arr, i+1, cnt+1, target, total+lst[i])

N, L, R, X = map(int, input().split())
lst = sorted(list(map(int, input().split())))
answer = 0
solve()