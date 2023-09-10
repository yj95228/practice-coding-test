# 1차 제출: 1 <= N <= 1000인데 날짜조건인줄 알고 1001까지 탐색 (114328kb, 132ms)
# 2차 제출: 367까지 탐색 (114328kb -> 120ms)
# https://www.acmicpc.net/problem/20207
import sys
sys.stdin = open('python/baekjoon/input.txt','r')
input = sys.stdin.readline

N = int(input())
arr = [0]*367
for _ in range(N):
    S, E = map(int, input().split())
    for i in range(S,E+1):
        arr[i] += 1
answer, width, height = 0, 0, 0
for i in range(1,367):
    if arr[i]:
        width += 1
        height = max(arr[i], height)
    else:
        answer += width*height
        width, height = 0, 0
print(answer)