# https://www.acmicpc.net/problem/1417
import sys

sys.stdin = open('input.txt','rt')
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
mx = max(arr[1:]) if len(arr) > 1 else 0
cnt = 0
while arr[0] <= mx:
    arr[arr[1:].index(mx)+1] -= 1
    arr[0] += 1
    mx = max(arr[1:])
    cnt += 1
print(cnt)