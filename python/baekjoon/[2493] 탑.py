# TODO: 다시 풀어보기
# https://www.acmicpc.net/problem/2493
import sys

sys.stdin=open("input.txt", "rt")
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
stack, answer = [], [0]*N
for i in range(N):
    while stack:
        if arr[stack[-1]] <= arr[i]:
            stack.pop()
        else:
            answer[i] = stack[-1]+1
            break
    stack.append(i)
print(*answer)

# 다시 풀기
for i, x in enumerate(arr):
    # 나보다 작은 탑은 가려짐
    while stack and x > arr[stack[-1]]:
        stack.pop()
    if stack: answer[i] = stack[-1]+1
    stack.append(i)
print(*answer)