# https://www.acmicpc.net/problem/6603
import sys
input = sys.stdin.readline

def dfs(n, start, arr):
    if n == 6:
        print(*arr)
        return
    for i in range(start, len(lotto)):
        dfs(n+1, i+1, arr+[lotto[i]])

while True:
    K, *lotto = map(int, input().split())
    if K == 0: break
    lotto = sorted(list(lotto))
    dfs(0,0,[])
    print()