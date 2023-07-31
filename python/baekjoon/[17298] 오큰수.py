# TODO: 다시 풀기
# https://www.acmicpc.net/problem/17298
import sys

sys.stdin=open("input.txt", "rt")
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
stack, answer = [], [-1]*N
for i in range(N-1, -1, -1):    # 오른쪽부터 왼쪽으로
    # 내가 오른쪽에 있는 숫자를 가리는 경우 : 쓸모없으므로 pop
    while stack and arr[i] > stack[-1]:
        stack.pop()
    if stack:
        answer[i] = stack[-1]
    stack.append(arr[i])
print(*answer)


# 다른 코드
stack, answer = [], [-1]*N
for i in range(len(arr)):
    while stack and arr[stack[-1]] < arr[i]:
        j = stack.pop()
        answer[j] = arr[i]
    stack.append(i)
print(*answer)