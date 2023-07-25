# https://www.acmicpc.net/problem/2018
import sys

sys.stdin=open("input.txt", "rt")
input = sys.stdin.readline
N = int(input())
arr = [i for i in range(1, N+1)]
answer = 0
left = 0
right = 1
sm = sum(arr[left:right])
while left < N:
    if sm == N:
        answer += 1
        left += 1
        right = left+1
        sm = sum(arr[left:right])
    elif sm < N:
        sm += arr[right]
        right += 1
    elif sm > N:
        sm -= arr[left]
        left += 1
print(answer)