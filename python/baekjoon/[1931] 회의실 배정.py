# https://www.acmicpc.net/problem/1931
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N = int(input())
arr = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: (-x[1], -x[0]))
print(arr)
answer, time = 0, 0
while arr:
    start, end = arr.pop()
    if time <= start:
        answer += 1
        time = end
print(answer)