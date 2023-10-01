# https://www.acmicpc.net/problem/15658
from sys import stdin
stdin = open('python/baekjoon/input.txt','r')
input = stdin.readline

def recur(n, result):
    global mn, mx
    if n == N:
        mn = min(mn, result)
        mx = max(mx, result)
        return
    
    if calc[0]:
        calc[0] -= 1
        recur(n+1, result+arr[n])
        calc[0] += 1

    if calc[1]:
        calc[1] -= 1
        recur(n+1, result-arr[n])
        calc[1] += 1

    if calc[2]:
        calc[2] -= 1
        recur(n+1, result*arr[n])
        calc[2] += 1

    if calc[3]:
        calc[3] -= 1
        if result >= 0:
            recur(n+1, result//arr[n])
        else:
            recur(n+1, -((-result)//arr[n]))
        calc[3] += 1

N = int(input())
arr = list(map(int, input().split()))
calc = list(map(int, input().split()))
mn, mx = 1_000_000_001, -1_000_000_001
recur(1, arr[0])
print(mx)
print(mn)